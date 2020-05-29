from flask import Flask, request, jsonify, send_from_directory,send_file
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

output=0
@app.route('/result',methods=['GET','POST'])
def result():
	global output
	x=request.get_json()
	link=x['url']
	print(link)

   
	video_url = link

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
	if(str(x[0].text).strip()=="Education"):
		if(c):
			output=1
		else:
			output=0
	else:
		output=-1
	print(output)
	return " "

@app.route('/res',methods=['GET','POST'])
def res():
    return jsonify({'result':output})

@app.route('/send',methods=['GET','POST'])
def send():
    return send_file('/home/smrnmakhija/brevis/backend/downloadfile.zip',attachment_filename='downloadfile.zip')
    


    

        


if __name__ == '__main__':
    app.run(debug=True)

