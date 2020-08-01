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
import time
import shutil

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")

def main():

	# Transcription and Cleaning
	url = input("Enter the URL = ")
	
	start = time.perf_counter()
	
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()
	
	# Keywords Extractor
	num_keywords = 10
	words=KeywordsExtractor(text,num_keywords)
	keywords = words.ExtractKeywords()
	print(f'\nKeywords:\n {keywords}')


	# Summarization    
	summ = Summarizer()
	percentage = 40
	summary_result = summ.summary(text,percentage)
	print(f'\nSummary:\n {summary_result}')
	

	# Keyframe Extraction (Output : 'out' folder)
	print("\nExtracting Keyframes\n")
	ip = ImageProcessing(url,keywords)
	ip.img_processing(text_threshold = 50, dis_threshold = 20, jump = 1500)
	print(len(os.listdir(os.path.join('res','out'))),"images extracted in 'out' folder")
	

	# Paragraph and Headings (Output : paragraph_headings.txt)
	print("\nGenerating Paragraphs and Headings\n")
	pf = ParaFormation(summary_result)
	list_para = pf.paragraph(similarity_threshold = 0.35,word_threshold = 20)
	ph = ParaHeadings(list_para)
	title_para = ph.get_titles_paras(sentence_threshold = 4,training = 200, heading_threshold = 3)
	

	# Final Notes (Includes Web Scraping) 
	print("\nGenerating Final Notes\n")   
	scraped_results = Scrapper(keywords,2,2,2)
	s = scraped_results.web_scrape()
	notes = Notes(url,s)
	notes.generate_notes()
	print("\nBrevis-Notes.docx and Brevis-Notes.pdf(on Windows) Generated\n")
	
	
	if os.path.exists('res'):
		shutil.rmtree('res')

	finish = time.perf_counter()
	print(f'Serial: Finished in {round(finish-start, 2)} second(s)')
	
if __name__ == '__main__':
	main()
