import sys
sys.path.append("utils")
#Importing all the files and necessary modules
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

#Process to extract keywords and run Image Processing and Web Scraping parallely
def Process_Extract_Keywords(url,text,Q):
	print("Extracting Keywords :-\n")
	num_keywords=10
	words=KeywordsExtractor(text,num_keywords).ExtractKeywords()
	print(f"\nKeywords : {words}\n")
	#Running Image Processing and Web Scraping in Parallel
	img_process = multiprocessing.Process(target=Process_Image_Extraction, args=(url,words,50,20,1000))
	scraping_process = multiprocessing.Process(target=Process_Web_Scraping,args=(words,2,2,2,Q))
	#Starting both the process simultaneously
	img_process.start()
	scraping_process.start()
	#Checking if the process have completed and printing the result
	img_process.join()
	scraping_process.join()
	
	
#Process to generate summary from the text and run Paragraph Formation and Paragraph Heading serially(Can't be run in parallel)
def Process_Get_Summary(text,percentage):
	print("Extracting Summary :-\n")
	summ = Summarizer().summary(text,percentage)
	print(f"\n Summary : {summ}\n")
	#Dividing Text into Paragraphs
	paras = ParaFormation(summ).paragraph(similarity_threshold = 0.35,word_threshold = 20)
	#Generating Headings for Paragraphs
	ParaHeadings(paras).get_titles_paras(sentence_threshold = 4,training = 200, heading_threshold = 3)

	
#Process to Extract keyframes and remove the non-text and similar images
def Process_Image_Extraction(url,words,text_threshold,dis_threshold,jump):
	print("Extracting Images - \n")
	ImageProcessing(url,words).img_processing(text_threshold,dis_threshold,jump)
	print(len(os.listdir(os.path.join('res','out'))),"images extracted in 'out' folder")

#Scraping the web to fetch links and adding those links to the multiprocessing queue
def Process_Web_Scraping(words,gres,yres,wres,Q):
	print("Scraping the Web for additional resources :- ")
	links = Scrapper(words,gres,yres,wres).web_scrape()
	print(f"Scraped Links : {links}\n")
	Q.put(links)


#The main driver function to be run.It will trigger other functions automatically.
def main():

	url = input("Enter the URL = ")
    #Starting the timer    
	start = time.perf_counter()
    
    # Transcription and Cleaning
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()

    #Declaring a multiprocessing queue to exchange data between various functions
	Q=multiprocessing.Queue()
    #Running keywords and summary Processes parallely
	key_ext=multiprocessing.Process(target=Process_Extract_Keywords , args=(url,text,Q))
	summ_ext=multiprocessing.Process(target=Process_Get_Summary , args=(text,40))
	#Starting both process simultaneously
	key_ext.start()
	summ_ext.start()
	#Checking if the process have finished execution
	key_ext.join()
	summ_ext.join()
	#Fetching scraped links from the Queue
	scraped_res = Q.get()
	
	#Generating final notes
	notes = Notes(url,scraped_res)
	notes.generate_notes()
	print("\nBrevis-Notes.docx and Brevis-Notes.pdf(on Windows) Generated\n")
	
	#Removing the temporary res folder
	if os.path.exists('res'):
	    shutil.rmtree('res')
	    
	#Stopping the timer  
	end=time.perf_counter()
	#Printing the time taken by the program for execution
	print(f"Finished in {round(end-start, 3)} second(s)")

if __name__ == "__main__":
	main()
