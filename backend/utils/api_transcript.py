# Assembly AI Account Details
# Username : tegon18992@netmail9.com
# password : abcd1234

#For testing must create a res folder in the same directory as the file

#Importing necessary modules
from __future__ import unicode_literals 
import youtube_dl
import shutil
import requests
import os
from pydub import AudioSegment
import sys
import time

class GenerateTranscript:
	def __init__(self,url):
		self.url = url

	def read_file(self,filename, chunk_size=5242880):
		with open(filename, 'rb') as _file:
			while True:
				data = _file.read(chunk_size)
				if not data:
					break
				yield data
				

	def generate_transcript(self):

		start = time.perf_counter()

		API_TOKEN = "b65450f72ec046eb94bb1cb93267e0c1"

		ydl_opts = {
		    'format': 'bestaudio',
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    info = ydl.extract_info(self.url, download=False)
		    audio_url = info['formats'][0]['url']
		    print(audio_url)
	    
	    
		check = r"https://manifest.googlevideo.com"  
		if audio_url[:len(check)] == check:
			print("Using audio file")
			if os.path.exists(os.path.join('res','audio')):
				shutil.rmtree(os.path.join('res','audio'))

			os.mkdir(os.path.join('res','audio'))

		    # Extract Audio From YouTube
			ydl_opts = {
		        'format': 'bestaudio/best',
		        'postprocessors': [{
		            'key': 'FFmpegExtractAudio',
		            'preferredcodec': 'mp3',
		            'preferredquality': '192'
		        }],
		        'postprocessor_args': [
		            '-ar', '16000'
		        ],
		        'prefer_ffmpeg': True,
		        'outtmpl':os.path.join('res','audio','test.mp3')
		    }

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])

			# Upload File
			filename = os.path.join('res','audio','test.mp3')
		    
		    
			headers = {'authorization': API_TOKEN}
			response = requests.post('https://api.assemblyai.com/v2/upload',
		                             headers=headers,
		                             data= self.read_file(filename))
		    
	    
			# Submit the audio file
			endpoint = "https://api.assemblyai.com/v2/transcript"

			json = {
			  "audio_url": response.json()['upload_url']
			}

			headers = {
			    "authorization": API_TOKEN,
			    "content-type": "application/json"
			}

			response = requests.post(endpoint, json=json, headers=headers)

			print(response.json())


		else:
			print("Using audio url")
			# Submit the audio url
			endpoint = "https://api.assemblyai.com/v2/transcript"

			json = {
			  "audio_url": audio_url
			}

			headers = {
			    "authorization": API_TOKEN,
			    "content-type": "application/json"
			}

			response = requests.post(endpoint, json=json, headers=headers)

			print(response.json())


		while(1):
			time.sleep(5)
			endpoint = "https://api.assemblyai.com/v2/transcript/"+response.json()['id']

			headers = {
				"authorization": API_TOKEN,
			}

			response = requests.get(endpoint, headers=headers)
			print(response.json()['status'])
			if(response.json()['status'] == 'completed'):
				text = response.json()['text']
				with open(os.path.join('res','transcript.txt'),'w') as f:
					f.write(text)
				print(f"Video Transcript :\n{text}\n")
				end = time.perf_counter()
				print(f"Transcript Generated in {round(end-start,2)} second(s).")
				return text



if __name__=="__main__":

	url = input("Enter video URL : ")
	transcript = GenerateTranscript(url).generate_transcript()
	print(f"\nTranscript : {transcript}\n")
