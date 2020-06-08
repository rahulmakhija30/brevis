# Input : YouTube URL (Ex : https://www.youtube.com/watch?v=8HyCNIVRbSU)
# Output : Extracted Frames from the video in the 'out' folder
# Time of execution : Around 5-6 min

'''
Parameters/Thresholds:
1) Number of keywords : n
2) Image Similarity : dis_threshold (Default : 20)
3) Non-Text Image : text_threshold (Default : 50) -> Len of the text
4) Jumping by 5000 ms to capture next frame
'''

# Import modules
from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
import io

from youtube_transcript_api import YouTubeTranscriptApi
import cv2
import os
import pafy
import youtube_dl
import numpy as np
import requests
import imageio
from PIL import Image
import pytesseract

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

def detect_text(img):
    text = pytesseract.image_to_string(img,lang='eng')
    return text

def frames(u,s,e):    
    url = u
    vPafy = pafy.new(url)
    play = vPafy.getbest()
    capture = cv2.VideoCapture(play.url)
    
#   capture = cv2.VideoCapture("video1.mp4")   

    _,frame = capture.read()
    start = s
    end = e
    start = start + 250
    global count
    while(start <= end):
        
        capture.set(cv2.CAP_PROP_POS_MSEC,start)
        _,frame = capture.read()
        
        if frame is None:
            start = start+250
            continue
            
        cv2.imwrite("out/image"+str(count)+".jpg", frame)
        count+=1
        
        start = start+5000
        prev_frame = frame
        
    capture.release()


def start_end(transcript,search):
    count=0
    duration=0
    start=0
    end=0
    new=0
    for i in range(len(transcript)):
        while count<len(search):
            if search[count] in transcript[i]['text'].strip().lower().split():
                count+=1
                continue
            elif count != 0:
                new=1
                break
            else:
                count=0
                break
        if(count==len(search)):
            res = ''
            if(new):
                start = transcript[i-1]['start']
                duration = transcript[i-1]['duration']
                duration += transcript[i]['duration']
                res = transcript[i-1]['text']
                res += transcript[i]['text']

            else:
                start = transcript[i]['start']
                duration = transcript[i]['duration']
                res = transcript[i]['text']

            end = start + duration
            break
            
    return int(start * 1000),int(end * 1000)

if __name__ == '__main__':
    url = input("Enter the URL : ")
    number_of_transciptions,transcripts = youtube_transcribe(url)

    if number_of_transciptions:
        with open("transcript.txt","w") as f:
        
                while number_of_transciptions > 0:
                    if '.' in transcripts[number_of_transciptions-1]:
                        text = transcripts[number_of_transciptions-1]
                        f.write(transcripts[number_of_transciptions-1])
                        break
                
                    if number_of_transciptions == 1:
                        text = transcripts[0]
                        f.write(transcripts[0])
                        
                    number_of_transciptions-=1
                    
        print("Transcription Done!!")
    else:
        print("No Transcript Available")

    # Keywords Extractor
    keywords=get_keywords(text,20)
    print('\nKeywords:\n',keywords)
    
    urlID = url.partition('https://www.youtube.com/watch?v=')[-1]
    transcript = YouTubeTranscriptApi.get_transcript(urlID)
    
    os.mkdir('out') 

    # Process Every Keyword
    count=0
    for key in range(len(keywords)):
        search = keywords[key].split()
        start,end = start_end(transcript,search)
        frames(url,start,end)
        
            
    # Remove non-text images
    print("Removing non-text images")
    text_threshold = 50
    files = os.listdir(r"out")
    for i in files:
        res = detect_text('out/'+i)
        if res == '' or len(res) < text_threshold :
            os.remove('out/'+i)
            
            
    # Remove Similar Images
    print("Removing Similar Images")
    dis_threshold = 20
    files = os.listdir(r"out")
    i=0
    while i<len(files)-1:
        r = requests.post(
            "https://api.deepai.org/api/image-similarity",
            files={
                'image1': open('out/'+files[i], 'rb'),
                'image2': open('out/'+files[i+1], 'rb'),
            },
            headers={'api-key': '08dd8c70-ad69-43aa-bd1d-01de53d8ebd6'}
        )
        res = r.json()
        
        dis = res['output']['distance']
        if dis >= dis_threshold:
            i+=2
        else:
            os.remove('out/'+files[i])
            i+=1