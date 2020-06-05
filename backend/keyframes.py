# Input : Youtube URL (Ex : https://www.youtube.com/watch?v=8HyCNIVRbSU)
# Output : Extracted Frames from the video in the 'out' folder
# Time of execution : Around 5-7 min

from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
import io

from youtube_transcript_api import YouTubeTranscriptApi
import cv2
import os
import pafy
import youtube_dl
import numpy as np

def frames(u,s,e):    
    p_frame_thresh = 1300000
    url = u
    vPafy = pafy.new(url)
    play = vPafy.getbest()
    capture = cv2.VideoCapture(play.url)
    start = s  #1s
    end = e #3s
    _,frame = capture.read()
    prev_frame = frame
    num = 0
    while(start <= end):
        capture.set(cv2.CAP_PROP_POS_MSEC,start)
        _,frame = capture.read()
        if frame is None:
            start = start+250
            continue
        diff = cv2.absdiff(frame, prev_frame)
        non_zero_count = np.count_nonzero(diff)
        if non_zero_count > p_frame_thresh:
            cv2.imwrite("out/image"+str(start)+".jpg", frame)
            num+=1
        start = start+250
        prev_frame = frame
    if num == 0: cv2.imwrite("out/image"+str(start)+".jpg", frame)
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
        with io.open("transcript.txt", "w", encoding="utf-8") as f:
            text = transcripts[0]
            f.write(transcripts[0])
            print("Transcription Done!!")
    else:
        print("No Transcript Available")

    # Keywords Extractor
    keywords=get_keywords(text,20)
    print('\nKeywords:\n',keywords)
    
    urlID = url.partition('https://www.youtube.com/watch?v=')[-1]
    transcript = YouTubeTranscriptApi.get_transcript(urlID)
    
    os.mkdir('out') 
    
    for key in range(len(keywords)):
        search = keywords[key].split()
        start,end = start_end(transcript,search)
        frames(url,start,end)