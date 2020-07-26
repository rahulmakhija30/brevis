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

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")

def main():    
    # Transcription and Cleaning
    url = input("Enter the URL = ")
    
    start = time.perf_counter()
    
    yt = YoutubeTranscribe(url)
    text = yt.youtube_transcribe()
    
    # Keywords Extractor
    # num_keywords=int(input("Enter number of keywords to be extracted : "))
    num_keywords=10
    words=KeywordsExtractor(text,num_keywords)
    keywords = words.ExtractKeywords()
    print(f'\nKeywords:\n {keywords}')

    # Summarization    
    summ = Summarizer()
    # percentage=int(input("Enter percentage of text you want as summary : "))
    percentage = 40
    summary_result = summ.summary(text,percentage)
    print(f'\nSummary:\n {summary_result}')
    
    # Keyframe Extraction (Output : 'out' folder)
    print("\nExtracting Keyframes\n")
    ip = ImageProcessing(url,keywords)
    ip.img_processing(jump=1000)
    print(f"\n{len(os.listdir(r'out'))} images extracted in 'out' folder\n")
    
    # Paragraph and Headings (Output : paragraph_headings.txt)
    print("\nGenerating Paragraphs and Headings\n")
    pf = ParaFormation(summary_result)
    list_para = pf.paragraph()
    ph = ParaHeadings(list_para)
    title_para = ph.get_titles_paras(sentence_threshold=2)
    
    # Final Notes (Includes Web Scraping) 
    print("\nGenerating Final Notes\n")   
    scraped_results = Scrapper(keywords,2,2,2)
    s = scraped_results.web_scrape()
    notes = Notes(url,s)
    notes.generate_notes()
    print("\nBrevis-Notes.docx Generated\n")
    
    finish = time.perf_counter()

    print(f'Serial: Finished in {round(finish-start, 2)} second(s)')
    
if __name__ == '__main__':
    main()