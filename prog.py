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

    # sample youtube video url
    video_url = link
# get the html content
    content = requests.get(video_url)
# create bs object to parse HTML
    soup = bs(content.content, "html.parser")
# write all HTML code into a file
    #open("video.html", "w", encoding='utf8').write(content.text)

    cards=(soup.find_all("ul", attrs={'class', 'watch-extras-section'}))

    for card in cards:
	    x=card.find_all("ul", attrs={'class', 'content watch-info-tag-list'})

    #print(x[0].text)
    if(str(x[0].text).strip()=="Education"):
        output=1
    else:
        output=0
    print(output)
    return " "

@app.route('/res',methods=['GET','POST'])
def res():
    print("fff", output)
    return jsonify({'result':output})

@app.route('/send',methods=['GET','POST'])
def send():
    print("v burvb")
    return send_file('/home/smrnmakhija/part-3/downloadfile.zip',attachment_filename='downloadfile.zip')
    #f = open('downloadfile.txt','r')
    #print("xx",f.read())
    #return 'downloadfile.txt'
    #return str(f.read())
    send_from_directory('/home/smrnmakhija/part-3','downloadfile.zip', as_attachment=True)
    return "Hello"


    

        


if __name__ == '__main__':
    app.run(debug=True)

