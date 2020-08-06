# Input : YouTube URL (Ex : https://www.youtube.com/watch?v=8HyCNIVRbSU)
# Output : Extracted Frames from the video in the 'out' folder
# Time of execution : Around 5-6 min

'''
Parameters/Thresholds:
1) Number of keywords : n
2) Image Similarity : dis_threshold (Default : 20)
3) Non-Text Image : text_threshold (Default : 50) -> Len of the text
4) Jumping by some milliseconds to capture next frame: jump (Default : 1500ms)
'''

# Import modules
from youtube_transcription import YoutubeTranscribe
from keywords_extractor import KeywordsExtractor
from youtube_transcript_api._errors import TranscriptsDisabled

from youtube_transcript_api import YouTubeTranscriptApi
from PIL import Image
import io
import cv2
import os
import pafy
import youtube_dl
import numpy as np
import requests
import imageio
import pytesseract
from sys import exit

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'


class ImageProcessing:
	def __init__(self,url,keywords):
		self.url = url
		self.keywords = keywords
	
	def detect_text(self,img):
		text = pytesseract.image_to_string(img,lang='eng')
		return text

	def frames(self,u,s,e,jump):    
		# URL
		url = u
		vPafy = pafy.new(url)
		play = vPafy.getbest()
		capture = cv2.VideoCapture(play.url)

		# Download
	#     ydl_opts = {'outtmpl': 'video.mp4','format': 'mp4'}
	#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	#         ydl.download([url])  
	#     capture = cv2.VideoCapture("video.mp4")   

		_,frame = capture.read()
		start = s
		end = e
		start = start + 250
		# global count
		while(start <= end):

			capture.set(cv2.CAP_PROP_POS_MSEC,start)
			_,frame = capture.read()

			if frame is None:
				start = start+250
				continue
			
			image_path = os.path.join('res','out','image'+str(start)+'.jpg')
			cv2.imwrite(image_path, frame)
			# count+=1

			start = start+jump
			prev_frame = frame

		capture.release()


	def start_end(self,transcript,search):
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

	def img_processing(self,text_threshold = 50,dis_threshold = 20,jump=1500):
		urlID = self.url.partition('https://www.youtube.com/watch?v=')[-1]
		
		try:
			transcript = YouTubeTranscriptApi.get_transcript(urlID)
		
		except TranscriptsDisabled as s:
			print("No images will be there in your notes")
			return

		#Fetching API Keys for Image Simmilarity API
		try:
			f=open("Image_Sim_API_Keys.txt","r")
		except Exception as e:
			print(e)
			exit(1)

		api_keys = f.read().split("\n")
		f.close()
		#print(api_keys)

		if not os.path.exists(os.path.join('res','out')):
			os.mkdir(os.path.join('res','out'))

		# Process Every Keyword
		count=0
		for key in range(len(self.keywords)):
			search = self.keywords[key].split()
			start,end = self.start_end(transcript,search)
			self.frames(self.url,start,end,jump)

		print(f"Initial : {len(os.listdir(os.path.join('res','out')))} images extracted in 'out' folder")

		# Remove non-text images
		print("Removing non-text images")
		files = os.listdir(os.path.join('res','out'))
		for i in files:
			res = self.detect_text(os.path.join('res','out',i))
			if res == '' or len(res) < text_threshold :
				os.remove(os.path.join('res','out',i))

		print(f"Number of Images After Removing Non Text Images : {len(os.listdir(os.path.join('res','out')))}")


		# Remove Similar Images
		print("Removing Similar Images")
		files = os.listdir(os.path.join('res','out'))
		i=0
		while i<len(files)-1:
			r = requests.post(
				"https://api.deepai.org/api/image-similarity",
				files={
					'image1': open(os.path.join('res','out',files[i]), 'rb'),
					'image2': open(os.path.join('res','out',files[i+1]), 'rb'),
				},
				headers={'api-key': api_keys[0]}
			)
			res = r.json()
			try:
				dis = res['output']['distance']

			except:
				api_keys.pop(0)
				if(len(api_keys)==0):
					print("All API Keys exhausted for Image Similarity.Please add new keys and try again.")
					try:
						f=open("Image_Sim_API_Keys.txt","w")
						f.write("")
						f.close()	
						exit(1)
					except Exception as e:
						print(e)
						exit(1)

				r = requests.post(
					"https://api.deepai.org/api/image-similarity",
					files={
						'image1': open(os.path.join('res','out',files[i]), 'rb'),
						'image2': open(os.path.join('res','out',files[i+1]), 'rb'),
					},
					headers={'api-key': api_keys[0]}
				)
				
				res = r.json()
				dis = res['output']['distance']


			if dis >= dis_threshold:
				i+=1
			else:
				os.remove(os.path.join('res','out',files[i]))
				i+=1

		print(f"Final : {len(os.listdir(os.path.join('res','out')))} images extracted in 'out' folder")


		#Writing the keys back to file
		try:
			f=open("Image_Sim_API_Keys.txt","w")
			if(len(api_keys)==1):
				f.write(api_keys[0])
				f.close()
			else:
				api_keys = '\n'.join(api_keys)
				#print(api_keys)
				f.write(api_keys)
				f.close()

		except Exception as e:
			print(e)
			exit(1)

				
if __name__ == '__main__':
	# Youtube Transcription
	url = input("Enter the URL = ")
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()
	
	# Keywords Extractor
	# num_keywords=int(input("Enter number of keywords to be extracted : "))
	num_keywords=10
	words=KeywordsExtractor(text,num_keywords)
	words.ExtractKeywords()
	keywords = words.keywords
	print('\nKeywords:\n',keywords)
	
	
	ip = ImageProcessing(url,keywords)
	ip.img_processing(text_threshold = 50,dis_threshold = 20,jump=1500)
