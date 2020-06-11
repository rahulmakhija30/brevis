from youtube_transcript_api import YouTubeTranscriptApi
from docx import Document
from docx.shared import Inches
import os
directory = os.getcwd()+'/out'

def add_picture(url):
	urlID = url.partition('https://www.youtube.com/watch?v=')[-1]
	transcript = YouTubeTranscriptApi.get_transcript(urlID)




	f1=open('summary.txt')
	summary=f1.read()

	f1.close()

	f=open("file1.txt","w")
	s=set()
	paras=[[i,[]]for i in summary.split('\n')]
	j=0
	for filename in os.listdir(directory):
		l=filename.split(".")
		time=float(l[0][5:])
		j=0
		while(j<len(transcript)):
			data=transcript[j]
			index=0
			if(time>=(data['start']*1000) and time<(((data['start']+data['duration'])*1000)+2000)):
				text=data['text'].replace('\n',' ')
				t=(text,time)
				while index <(len(paras)):
					if(text in paras[index][0]):
						if(filename not in paras[index][1]):
							paras[index][1].append(filename)
						break
			
					index+=1
			j+=1

	document = Document()

	p = document.add_paragraph()
	r = p.add_run()
	for para in paras:
		if(para[0]):
			f.write(para[0])
			r.add_text(para[0])
			f.write("\n\n")
			r.add_text("\n\n")
		if(para[1]):
			for name in para[1]:
				r.add_picture(directory+'/'+name,width=Inches(3.0))
				f.write(name)
				f.write("\n")
				r.add_text('\n')
	document.save('test10.docx')
	f.close()

#add_picture('https://www.youtube.com/watch?v=ESusD8HRLBI&list=PLAD5B880806EBE0A4&index=64')

