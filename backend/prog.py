from flask import Flask, request,jsonify,send_file
import requests
from bs4 import BeautifulSoup as bs
from youtube_transcription import youtube_transcribe
#from keywords_extractor import get_keywords
from summary_generator import summary
#import io
from zipfile import ZipFile
import os.path

app = Flask(__name__)

output=0
videourl="https://www.youtube.com/watch?v=xR2DPnyLEE0"
path=""
video_url=""
x=""


def generate(data):
	global video_url
	global path
	#url = input("Enter the URL = ")
	number_of_transciptions,transcripts = youtube_transcribe(video_url)

	if number_of_transciptions:
		#with io.open("transcript.txt", "w", encoding="utf-8") as f:
		text = transcripts[0]
		#f.close()
			#f.write(transcripts[0])
			#print("Transcription Done!!")
	#else:
		#print("No Transcript Available")

    # Keywords Extractor
	#keywords=get_keywords(text,15)
	#print('\nKeywords:\n',keywords)

    # Summarization
	result = summary(text,60)
	#print('\nSummary:\n',result)
	fh=open("summary.txt","w")
	fh.write(result)
	fh.close()
	with ZipFile('brevis_notes2.zip','w') as zip:
		print("Writing zip")
		zip.write("summary.txt") 
	zip.close()
	path=os.path.abspath("brevis_notes2.zip")
	#f=open("brevis_notes.zip",w)
	#f.close()
	

	




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
	print("this is res")
	print(video_url)
	return jsonify({'result':output})
    
@app.route('/download',methods=['GET','POST'])
def download():
	global output
	print("this is download")
	x=request.get_json()
	data=x['value']
	print("JJJJ",data,output)
	print("hthtg",x)
	if(output ==1):
		generate(data)
	#send_file("/home/smrnmakhija/brevis/backend/brevis_notes2.zip",attachment_filename='brevis_notes2.zip')
	return jsonify({'result':output})
	
	
	

@app.route('/send/<x>',methods=['GET','POST'])
def send(x):
	#x=request.get_json()
	global path
	print("this is send")
	return send_file("/home/smrnmakhija/brevis/backend/brevis_notes2.zip",attachment_filename='brevis_notes2.zip')
	#return " Hey"
	


    

        


if __name__ == '__main__':
    app.run(debug=True)

