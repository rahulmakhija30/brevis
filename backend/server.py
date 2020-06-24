from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
from keyframes import Image_Processing
from paragraph_headings import paragraph,get_titles_paras
from notes import add_picture
from web_scraping import web_scrape
from flask import Flask, request,jsonify,send_file
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile

import requests
import os.path
import operator
import paragraph_headings
import notes
import io
import os
import pytesseract

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

output=0
path=""
video_url=""
x=""
json_result=dict()
keywords=[]
text=""


def generate(data):
	global video_url
	global path
	global json_result
	global keywords
	global text
    global result
    
    # Transcription and Cleaning
	text = youtube_transcribe(video_url)
        
    # Keywords Extractor
	keywords=get_keywords(text,15)
	print('\nKeywords:\n',keywords)
	fp=open("keywords.txt","w")
	fp.write("\n".join(keywords))
	fp.close()
	json_result=web_scrape(keywords)
    
    # Summarization
    # Percentage of summary - input
    # percentage=int(input())
	result = summary(text,50)
	fh=open("summary.txt","w")
	fh.write(result)
	fh.close()
    
	#with ZipFile('brevis_notes2.zip','w') as zip:
	#	print("Writing zip")
	#	zip.write("summary.txt") 
	#	zip.write("keywords.txt")
	#zip.close()
	#path=os.path.abspath("brevis_notes2.zip")
	
	# Keyframe Extraction
	#Image_Processing(video_url,keywords)
	#print("Images Extracted in 'out' folder")
	    
	# Text Recognition And Extraction
	#text_recognition()
	#print("Cropped Text Extracted in 'crop' folder")

def gen():
	global video_url
	global keywords
	global path
	global json_result
	global text
    global result
    
    # Keyframe Extraction (Output : 'out' folder)
	Image_Processing(video_url,keywords)
	print(len(os.listdir(r"out")),"images extracted in 'out' folder")
    
    # Paragraph and Headings (Output : paragraph_headings.txt)    
	list_para = paragraph(result)
    title_para = get_titles_paras(list_para)
    
    # Final Notes - To be added (Refer : main.py)
	add_picture(video_url,json_result)
	print("Notes Generated")
	
    
	with ZipFile('brevis_notes.zip','w') as zip:
		print("Writing zip")
		zip.write("Brevis-Notes.docx") 
	zip.close()
	path=os.path.abspath("brevis_notes.zip")
	

	


@app.route('/result',methods=['GET','POST'])
def result():
	global output
	global video_url
	x=request.get_json()
	link=x['url']
	print(x)
	print(link)

   
	video_url = link

	content = requests.get(video_url)

	soup = bs(content.content, "html.parser")

	"""cards=(soup.find_all("ul", attrs={'class', 'watch-extras-section'}))

	for card in cards:
		x=card.find_all("ul", attrs={'class', 'content watch-info-tag-list'})"""

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
	return " "

@app.route('/res',methods=['GET','POST'])
def res():
	return jsonify({'result':output})
    
@app.route('/download',methods=['GET','POST'])
def download():
	global output
	x=request.get_json()
	data=x['value']
	if(output ==1):
		generate(data)
	print(json_result)
	return jsonify(json_result)
@app.route('/down',methods=['GET','POST'])
def down():
	global output
	if(output==1):
		print("in down")
		gen()
	return jsonify({'result':output})
		
	
@app.route('/send/<x>',methods=['GET','POST'])
def send(x):
	global path
	return send_file(path,attachment_filename='brevis_notes.zip')

	


    

        


if __name__ == '__main__':
    app.run(debug=True)

