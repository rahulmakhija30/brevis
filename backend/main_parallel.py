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

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import time

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

print("All Modules Imported Sucessfully")

def main():
    # Parallel
    url = input("Enter the URL = ")
    
    start = time.perf_counter()
    
    # Transcription and Cleaning
    yt = YoutubeTranscribe(url)
    text = yt.youtube_transcribe()

    # Level1
    with ThreadPoolExecutor() as executor:
        '''
        Type1:
        level1_results1 = executor.submit(Test(10,20).RecArea)
        print(type(level1_results1))
        print(dir(level1_results1))
        print(level1_results1.result())
        
        Type2:
        level1_results1 = list(executor.map(Test().RecArea,[10],[20]))
        print(level1_results1[0])
        '''
        
        # Keywords Extractor
        # num_keywords=int(input("Enter number of keywords to be extracted : "))
        num_keywords=10
        level1_results1 = executor.submit(KeywordsExtractor(text,num_keywords).ExtractKeywords)
        
        # Summarization  
        percentage = 40
        level1_results2 = list(executor.map(Summarizer().summary,[text],[percentage]))

        print(f"\nKeywords:\n {level1_results1.result()}")
        print(f"\nSummary:\n {level1_results2[0]}")

    
    # Level2
    with ThreadPoolExecutor() as executor:
        # Keyframe Extraction (Output : 'out' folder)
        print("\nExtracting Keyframes\n")
        level2_results1 = list(executor.map(ImageProcessing(url,level1_results1.result()).img_processing,[50],[20],[1000]))      
        
        # Paragraph and Headings (Output : paragraph_headings.txt)
        print("\nGenerating Paragraphs and Headings\n")
        level2_results2 = executor.submit(ParaFormation(level1_results2[0]).paragraph)
        
        print("\nScraping Web\n")    
        level2_results3 = executor.submit(Scrapper(level1_results1.result(),2,2,2).web_scrape)
        

        print(f"\n{len(os.listdir(r'out'))} images extracted in 'out' folder\n")
    
    
    ph = ParaHeadings(level2_results2.result())
    title_para = ph.get_titles_paras(sentence_threshold=2)

    # Final Notes
    notes = Notes(url,level2_results3.result())
    notes.generate_notes()
    print("\nBrevis-Notes.docx Generated\n")

    finish = time.perf_counter()

    print(f'Parallel: Finished in {round(finish-start, 2)} second(s)')
    
    
if __name__ == '__main__':
    main()
