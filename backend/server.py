import sys
sys.path.append("utils")

from youtube_transcription import YoutubeTranscribe
from google_speech_to_text import SpeechToText
from clean_transcript import CleanTranscript
from clean_transcript import *
from keywords_extractor import KeywordsExtractor
from summary_generator import Summarizer
from keyframes_extractor import ImageProcessing
from paragraph_headings import ParaFormation,ParaHeadings
from web_scraping import Scrapper
from notes import Notes
import paragraph_headings
import notes
import pafy
from flask import Flask, request,jsonify,send_file
from flask_socketio import SocketIO, emit,send
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile

from flask_cors import CORS
import requests
import re
import os.path
import operator

import io
import os
import pytesseract
import time
import shutil
import platform
import pafy

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins='*',timeout=3600000,ping_timeout=14400,ping_interval=7200)
#socketio = SocketIO(app,cors_allowed_origins='*',timeout=3600000)
print("This is socketio",socketio)
#CORS(app)

app.debug=True

app.host='localhost'


output=0
path=""
video_url=""
x=""
json_result=dict()
keywords=[]
text=""

# data: Information about type of notes required by the user

def generate(data):
	global video_url
	global path
	global json_result
	global keywords
	global text
	global summary_result
	global scrape_json
	global option
	option = data

	sec = pafy.new(video_url).length
	print(f"\nVideo duration in sec = {sec}\n")
	
	# THRESHOLDS
	
	if sec <= 900: # 0-15 min
		NUM_KEYWORDS = 15
		SUMMARY_PERCENT = 60
	
	elif 900 < sec <= 1800: # 15-30 min
		NUM_KEYWORDS = 18
		SUMMARY_PERCENT = 50 

	elif 1800 < sec <= 2700: # 30-45 min
		NUM_KEYWORDS = 20
		SUMMARY_PERCENT = 40
   
	elif 2700 < sec <= 3600: # 45-60 min
		NUM_KEYWORDS = 22
		SUMMARY_PERCENT = 35
	
	elif 3600 < sec <= 7200: # 1-2 hr
		NUM_KEYWORDS = 25
		SUMMARY_PERCENT = 30
		
	else: # More than 2 hr
		NUM_KEYWORDS = 30
		SUMMARY_PERCENT = 25

	
	start = time.perf_counter()

	# Transcription and Cleaning
	yt = YoutubeTranscribe(video_url)
	text = yt.youtube_transcribe()


	# Keywords Extractor
	# num_keywords=int(input("Enter number of keywords to be extracted : "))
	num_keywords = NUM_KEYWORDS
	words = KeywordsExtractor(text,num_keywords)
	keywords = words.ExtractKeywords()
	scrape_keywords = words.ExtractScrapeKeywords()
	print(f'\nKeywords:\n {keywords}')
	print(f'\nScrape Keywords:\n {scrape_keywords}')

	# fp=open("keywords.txt","w")
	# fp.write("\n".join(keywords))
	# fp.close()
	
	scraped_results = Scrapper(scrape_keywords,2,2,2)
	json_result = scraped_results.web_scrape()
	#print(json_result)
	scrape_json = json_result

	# Summarization    
	summ = Summarizer()
	percentage = SUMMARY_PERCENT

	# if option == "Overview":
	# 	percentage = 50
	
	# elif option == "Notes":
	# 	percentage = 60
	
	# elif option == "Notes+Ref":
	# 	percentage = 80
		
	summary_result = summ.summary(text,percentage)
	print(f'\nSummary:\n {summary_result}')

	# fh = open(os.path.join('res', "summary.txt"),"w")
	# fh.write(summary_result)
	# fh.close()

	finish = time.perf_counter()

	print(f'Generate Function: Finished in {round(finish-start, 2)} second(s)')

	
def gen():
	global video_url
	global keywords
	global path
	global json_result
	global text
	global summary_result
	global scrape_json
	global option

	sec = pafy.new(video_url).length
	print(f"\nVideo duration in sec = {sec}\n")
	
	# THRESHOLDS
	
	DYNAMIC_INTERVAL = (sec/60) * 100
	
	if sec <= 900: # 0-15 min
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3
	
	elif 900 < sec <= 1800: # 15-30 min
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20 
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3

	elif 1800 < sec <= 2700: # 30-45 min
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3
   
	elif 2700 < sec <= 3600: # 45-60 min
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3
	
	elif 3600 < sec <= 7200: # 1-2 hr
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3
		
	else: # More than 2 hr
		NON_TEXT_LEN = 50
		SIMILAR_DISTANCE = 20
		INTERVAL_KEYFRAMES = DYNAMIC_INTERVAL
		SENTENCE_SIMILARITY = 0.35
		WORDS_PER_PARA = 20
		PERCENT_REDUCE = 0.6
		SENTENCES_PER_PARA = 6
		HEADING_TRAINING = 500
		TOP_HEADINGS = 3

	start = time.perf_counter()
	
	if option == "Overview":
		if not os.path.exists(os.path.join('res','out')):
			os.mkdir(os.path.join('res','out'))
	
	elif option == "Notes" or option == "Notes+Ref":
		# Keyframe Extraction (Output : 'out' folder)
		print("\nExtracting Keyframes\n")
		ip = ImageProcessing(video_url,keywords)
		ip.img_processing(text_threshold = NON_TEXT_LEN, dis_threshold = SIMILAR_DISTANCE, jump = INTERVAL_KEYFRAMES)


	# Paragraph and Headings (Output : paragraph_headings.txt)
	print("\nGenerating Paragraphs and Headings\n")
	pf = ParaFormation(summary_result)
	list_para = pf.paragraph(similarity_threshold = SENTENCE_SIMILARITY, word_threshold = WORDS_PER_PARA, percent_reduce = PERCENT_REDUCE)
	ph = ParaHeadings(list_para)
	title_para = ph.get_titles_paras(sentence_threshold = SENTENCES_PER_PARA, training = HEADING_TRAINING, heading_threshold = TOP_HEADINGS)


	# Final Notes (Includes Web Scraping) 
	print("\nGenerating Final Notes\n")   
	
	if option == "Overview" or option == "Notes":
		scrape_json = {}
	
	#scraped_results = Scrapper(scrape_keywords,2,2,2)
	#s = scraped_results.web_scrape()
	notes = Notes(video_url,scrape_json)
	notes.generate_notes()
	print("\nBrevis-Notes.docx Generated\n")
	
	
	with ZipFile('Brevis_Notes.zip','w') as zip:
		print("Writing zip")
		if os.path.exists(os.path.join('res','Brevis-Notes.pdf')):
			zip.write(os.path.join('res','Brevis-Notes.pdf'),arcname='Brevis-Notes.pdf')
		zip.write(os.path.join('res','Brevis-Notes.docx'),arcname='Brevis-Notes.docx')
	
	path = os.path.abspath("Brevis_Notes.zip")

	if os.path.exists('res'):
		shutil.rmtree('res')

	finish = time.perf_counter()

	print(f'Gen Function: Finished in {round(finish-start, 2)} second(s)')



@socketio.on('connect')
def test_connect():
	print("connected")
	emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
	print('Client disconnected')


@app.route('/result',methods=['GET','POST'])
def result():
	global output
	global video_url
	x=request.get_json()
	link=x['url']
	print(x)
	print(link)

   
	video_url = link

	"""
	content = requests.get(video_url)

	soup = bs(content.content, "html.parser")

	cards=(soup.find_all("ul", attrs={'class', 'watch-extras-section'}))

	for card in cards:
		x=card.find_all("ul", attrs={'class', 'content watch-info-tag-list'})

	transcripts=(soup.find_all("div",attrs={'class','hid'}))

	c=0
	for transcript in transcripts:
		if('Transcript' in transcript.text):
			c=1

	#print(x[0].text)
	#if(str(x[0].text).strip()=="Education"):
	if(c):
		output=1
	else:
		output=0
	#else:
		#output=-1
	#print(output)
	
	"""
	
	if((re.match("^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$",video_url))):
		try:
			video = pafy.new(video_url)
			print(video.author)
			print(video.title)
			output=1
		except:
			print("Invalid video id(pafy)")
			output=0
		print("Done")
    

	else:
		print("Invalid link(regex)")
		output=0
	return " "

@app.route('/res',methods=['GET','POST'])
def res():
	return jsonify({'result':output})
	

@socketio.on('event1')
def download(x):
	global output
	print(x)
	data=x['type']
	print(data)
	if(output==1):
		generate(data)
	print(json_result)
	#emit('myresponse',{'data':'generate'},callback=ack)
	#send("done")
	emit('response1',json_result)
	print("sent")

@socketio.on('event2')
def down(z):
	global output
	if(output==1):
		print("in event2")
		gen()
	emit('response2',{'task':'done'})

	
@app.route('/send/<x>',methods=['GET','POST'])
def send(x):
	global path
	return send_file(path,attachment_filename='Brevis_Notes.zip')



if __name__ == '__main__':
	socketio.run(app)
