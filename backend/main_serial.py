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
import pafy

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")

# Default Thresholds (11)
# NUM_KEYWORDS = -
# SUMMARY_PERCENT = -
# NON_TEXT_LEN = 50
# SIMILAR_DISTANCE = 20 
# INTERVAL_KEYFRAMES = 1500
# SENTENCE_SIMILARITY = 0.35
# WORDS_PER_PARA = 20
# PERCENT_REDUCE = 0.6
# SENTENCES_PER_PARA = 5
# HEADING_TRAINING = 500
# TOP_HEADINGS = 3


def main():

	# Transcription and Cleaning
	url = input("Enter the URL = ")
	
	sec = pafy.new(url).length
	print(f"\nVideo duration in sec = {sec}\n")
	
	# THRESHOLDS
	
	DYNAMIC_INTERVAL = (sec/60) * 100
	
	if sec <= 900: # 0-15 min
		NUM_KEYWORDS = 15
		SUMMARY_PERCENT = 60
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
		NUM_KEYWORDS = 18
		SUMMARY_PERCENT = 50 
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
		NUM_KEYWORDS = 20
		SUMMARY_PERCENT = 40
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
		NUM_KEYWORDS = 22
		SUMMARY_PERCENT = 35
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
		NUM_KEYWORDS = 25
		SUMMARY_PERCENT = 30
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
		NUM_KEYWORDS = 30
		SUMMARY_PERCENT = 25
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
	
	yt = YoutubeTranscribe(url)
	text = yt.youtube_transcribe()
	
	# Keywords Extractor
	num_keywords = NUM_KEYWORDS
	words=KeywordsExtractor(text,num_keywords)
	keywords = words.ExtractKeywords()
	print(f'\nKeywords:\n {keywords}')


	# Summarization    
	summ = Summarizer()
	percentage = SUMMARY_PERCENT
	summary_result = summ.summary(text,percentage)
	print(f'\nSummary:\n {summary_result}')
	

	# Keyframe Extraction (Output : 'out' folder)
	print("\nExtracting Keyframes\n")
	ip = ImageProcessing(url,keywords)
	ip.img_processing(text_threshold = NON_TEXT_LEN, dis_threshold = SIMILAR_DISTANCE, jump = INTERVAL_KEYFRAMES)
	

	# Paragraph and Headings (Output : paragraph_headings.txt)
	print("\nGenerating Paragraphs and Headings\n")
	pf = ParaFormation(summary_result)
	list_para = pf.paragraph(similarity_threshold = SENTENCE_SIMILARITY, word_threshold = WORDS_PER_PARA, percent_reduce = PERCENT_REDUCE)
	ph = ParaHeadings(list_para)
	title_para = ph.get_titles_paras(sentence_threshold = SENTENCES_PER_PARA, training = HEADING_TRAINING, heading_threshold = TOP_HEADINGS)
	

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