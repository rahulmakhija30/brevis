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

import io
import os
import pytesseract
import shutil

import multiprocessing
import time

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")

#All process functions to be run in parallel
def Process_Extract_Keywords(url,text,Q):
	print("Extracting Keywords :-\n")
	num_keywords=10
	# global words
	words=KeywordsExtractor(text,num_keywords).ExtractKeywords()
	print(words)
	img_process = multiprocessing.Process(target=Process_Image_Extraction, args=(url,words,50,20,1000))
	scraping_process = multiprocessing.Process(target=Process_Web_Scraping,args=(words,2,2,2,Q))
	img_process.start()
	scraping_process.start()
	img_process.join()
	scraping_process.join()
	
	

def Process_Get_Summary(text,percentage):
	print("Extracting Summary :-\n")
	# global summ
	summ = Summarizer().summary(text,percentage)
	print(summ)
	paras = ParaFormation(summ).paragraph()
	ParaHeadings(paras).get_titles_paras(sentence_threshold=2)
	

def Process_Image_Extraction(url,words,text_threshold,dis_threshold,jump):
	print("Extracting Images - \n")
	ImageProcessing(url,words).img_processing(text_threshold,dis_threshold,jump)
	print(len(os.listdir(os.path.join('res','out'))),"images extracted in 'out' folder")

def Process_Web_Scraping(words,gres,yres,wres,Q):
	print("Scraping the Web for additional resources :- ")
	# global links
	links = Scrapper(words,gres,yres,wres).web_scrape()
	print(links)
	Q.put(links)

# def Process_Generate_Headings(summary):
# 	paras = 

#Main Function()
def main():
	#Parallel execution using multiprocessing
	url = input("Enter the URL = ")
    
	start = time.perf_counter()
    
    # Transcription and Cleaning
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()

    #Extracting keywords and summary parallely
	Q=multiprocessing.Queue()

	key_ext=multiprocessing.Process(target=Process_Extract_Keywords , args=(url,text,Q))
	summ_ext=multiprocessing.Process(target=Process_Get_Summary , args=(text,60))
	key_ext.start()
	summ_ext.start()
	key_ext.join()
	summ_ext.join()
	scraped_res = Q.get()
	print("Results : ",scraped_res)
	notes = Notes(url,scraped_res)
	notes.generate_notes()
	print("\nBrevis-Notes.docx Generated\n")

	if os.path.exists('res'):
	    shutil.rmtree('res')
	# l=list()
	# l.append(key_ext)
	# l.append(summ_ext)

	# for p in l:
	# 	p.start()

	# for p in l:
	# 	p.join()
	# # key_ext.start()
	# # summ_ext.start()
	# unsorted_res = [Q.get() for p in l]
	# result=[t[1] for t in sorted(unsorted_res)]
	# print("Keywords : ",result[0])
	# print("Summary : ",result[1])
	# #Checking if the keyword extraction has finished
	# key_ext.join()
	# summ_ext.join()
	#Triggering Image Processing and Scraping once Keywords are Extracted
	
	# ip = ImageProcessing(url,words)
	# ip.img_processing(jump=1000)
	

	

	
	# scrape_res=Q.get()
	# print(scrape_res)

	end=time.perf_counter()
	print(f"Finished in {round(end-start, 3)} second(s)")

if __name__ == "__main__":
	main()
