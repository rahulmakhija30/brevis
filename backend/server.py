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
path=""
video_url=""
x=""


def generate(data):
	global video_url
	global path
	number_of_transciptions,transcripts = youtube_transcribe(video_url)

	if number_of_transciptions:
		text = transcripts[0]
    # Keywords Extractor
	#keywords=get_keywords(text,15)
	#print('\nKeywords:\n',keywords)

    # Summarization
	result = summary(text,60)
	fh=open("summary.txt","w")
	fh.write(result)
	fh.close()
	with ZipFile('brevis_notes2.zip','w') as zip:
		print("Writing zip")
		zip.write("summary.txt") 
	zip.close()
	path=os.path.abspath("brevis_notes2.zip")
	

	




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
	return jsonify({'result':output})
	
	
	

@app.route('/send/<x>',methods=['GET','POST'])
def send(x):
	global path
	return send_file(path,attachment_filename='brevis_notes2.zip')

	


    

        


if __name__ == '__main__':
    app.run(debug=True)

