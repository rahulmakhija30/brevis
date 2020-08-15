from __future__ import unicode_literals
import speech_recognition as sr
import os
from os import path
import pydub
from pydub import AudioSegment
from pydub.effects import normalize
from pydub.playback import play
from pydub.utils import which
import youtube_dl
import traceback
from speech_recognition import RequestError
import shutil

if os.system("ffmpeg"):
	print("ffmpeg installed")
else:
	print("Please install ffmpeg from : https://www.ffmpeg.org/download.html")
		


class SpeechToText:
	
	def __init__(self,url):
		AudioSegment.converter = which("ffmpeg")
		self.url = url

	def speech_to_text(self):
		text = ''
		try:
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
				ydl.download([self.url])

			# convert mp3 file to wav 
			sound = AudioSegment.from_file(os.path.join('res','audio','test.mp3'))
			sound.export(os.path.join('res','audio','test.wav'), format="wav")

			s = AudioSegment.from_file(os.path.join('res','audio','test.wav'))
			s = s+10
			s = normalize(s)
			s.export(os.path.join('res','audio','test.wav'),format="wav")
			# transcribe audio file
			AUDIO_FILE = os.path.join('res','audio','test.wav') 

			# use the audio file as the audio source
			r = sr.Recognizer()
			with sr.AudioFile(AUDIO_FILE) as source:
					audio = r.record(source)  # read the entire audio file

					text = r.recognize_google(audio)

					with open(os.path.join('res','transcript.txt') , 'w') as f:
							f.write(text)

					return text        

		except RequestError as r:
			print("Recognition request failed: Bad Request")

		except PermissionError as p:
			print(p,"\nRe-run your program")

		except Exception as e:
			print("Error in Google Speech to Text")
			print(e)
			traceback.print_exc()

		finally:
			if os.path.exists(os.path.join('res','audio')):
				shutil.rmtree(os.path.join('res','audio'))
			return text
		
	
if __name__ == '__main__':
	url = input()
	st = SpeechToText(url)
	text = st.speech_to_text()
	print(text)