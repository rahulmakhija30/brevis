# Import Modules
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptAvailable
from youtube_transcript_api._errors import TranscriptsDisabled
from youtube_transcript_api._errors import *
from requests import ConnectionError

from urllib import parse
import requests
import traceback
import re
import os

from google_speech_to_text import SpeechToText
from clean_transcript import CleanTranscript
from clean_transcript import *

from api_transcript import *

class MyException(Exception):
	pass

try:
	if not(os.system("ffmpeg -version")):
		print("ffmpeg exists")
	else:
		raise MyException("ffmpeg not found")
except Exception as e:
	print(e)
	print("Install ffmpeg from : https://www.ffmpeg.org/download.html")
	

class YoutubeTranscribe:
	
	def __init__(self,url):
		self.url = url
		
		# Format URL
		first = 'https://www.youtube.com/watch?v='
		temp = url.partition(first)
		self.url = first + temp[-1][:11]
		
		
	def youtube_transcribe(self):
		text = ''
		
		if not os.path.exists('res'):
			os.mkdir('res')
			
		try:
			urlID = self.url.partition('https://www.youtube.com/watch?v=')[-1]

			transcript_list = YouTubeTranscriptApi.list_transcripts(urlID)

			t = list(transcript_list)

			for i in range(len(t)):
				if t[i].language_code == 'en':

					# Manually Created
					if not(t[i].is_generated):
						print("Got Manually Created Transcript")
						data = t[i].fetch()
						res=''
						for i in data:
							res = res + ' ' + i['text']

						print("Cleaning Manually Created Transcript")
						text = res.replace('\n',' ')
						text = text.strip()
						break

					# Auto-generated 
					if i == len(t)-1 and t[i].is_generated:
						print("Got Auto-generated Transcript")
						
						print("Using API to generate transcript")
						
						#API Calling and Transcript Generation
						text = GenerateTranscript(self.url).generate_transcript()
						
# 						except:
# 							print("Using YouTubes Transcript")

# 							data = t[i].fetch()
# 							res=''
# 							for i in data:
# 								res += i['text']

# 							print("Cleaning Auto-generated Transcript")
# 							text = res.replace('\n',' ')
# 							clean_trans=CleanTranscript(text)
# 							clean_trans.add_punctuations(punct_model)
# 							clean_trans.correct_mistakes(lang_model)
# 							text = clean_trans.text


		# No Transcript
		except NoTranscriptAvailable as t:
			print("No Transcript Available - Trying to generate one!!") 
			
			print("Using API")
			text = GenerateTranscript(self.url).generate_transcript()
				
# 			except:
# 				print("Using Google Speech To Text")
				
# 				st = SpeechToText(self.url)
# 				text = st.speech_to_text()

# 				print("Cleaning Transcript")         
# 				clean_trans=CleanTranscript(text)
# 				clean_trans.add_punctuations(punct_model)
# 				clean_trans.correct_mistakes(lang_model)
# 				text = clean_trans.text

		except TranscriptsDisabled as s:
			print("Subtitles are disabled for this video - Trying to generate one!!")
			
			print("Using API")
			text = GenerateTranscript(self.url).generate_transcript()                
				
# 			except:
# 				print("Using Google Speech To Text")
				
# 				st = SpeechToText(self.url)
# 				text = st.speech_to_text()

# 				print("Cleaning Transcript")         
# 				clean_trans=CleanTranscript(text)
# 				clean_trans.add_punctuations(punct_model)
# 				clean_trans.correct_mistakes(lang_model)
# 				text = clean_trans.text           

		# Other Errors
		except VideoUnavailable as v:
			print("Video is not available")

		except ConnectionError as c:
			print("No Internet")

		except Exception as e:
			traceback.print_exc()
			print(e)

		finally:
			text = re.sub("[\[].*?[\]]", "", text).strip()

			with open(os.path.join('res',"transcript.txt"),"w",encoding="utf-8") as f:
				f.write(text)
		
			if text == '': 
				print("No Transcript")
				return ''

			else: 
				print("Transcription and Cleaning Done!!")                
				return text
		
if __name__ == '__main__':
	# Testing
	# Manually Created Transcript - https://www.youtube.com/watch?v=b_sQ9bMltGU
	# Auto-generated Transcript - https://www.youtube.com/watch?v=1a8d3rWQPhg&t=3s
	# No transcript - https://www.youtube.com/watch?v=kthmIlrRswc
	# Invalid - https://www.youtube.com/channel/UCsFmLpSNJuFzpKqdEj5jeHw
	# Other - https://www.youtube.com/watch?v=b_sQ9bMltGU&list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG
	url = input("Enter the URL = ")
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()
	print(text)
