from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
from keyframes import Image_Processing
from paragraph_headings import paragraph,get_titles_paras
from notes import add_picture
from web_scraping import web_scrape

import paragraph_headings
import notes
import io
import os
import pytesseract

import logging
logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import time

if __name__ == '__main__':  
    # Parallel
    url = input("Enter the URL = ")
    
    start = time.perf_counter()

    text = youtube_transcribe(url)

    # Level1
    with ThreadPoolExecutor() as executor:
        # keywords = get_keywords(text,15)
        # result = summary(text,40)
        level1_results1 = list(executor.map(get_keywords,[text],[15]))
        level1_results2 = list(executor.map(summary,[text],[40]))

        print(f"Keywords: {level1_results1[0]}")
        print(f"Summary: {level1_results2[0]}")

    
    # Level2
    with ThreadPoolExecutor() as executor:
        # Image_Processing(url,keywords)
        # list_para = paragraph(result)
        # s=web_scrape(keywords)
        print("Extracting Keyframes")
        level2_results1 = list(executor.map(Image_Processing,[url],[level1_results1[0]]))

        print("Generating Paragraphs and Headings")
        level2_results2 = list(executor.map(paragraph,[level1_results2[0]]))
        level2_results3 = list(executor.map(web_scrape,[level1_results1[0]]))

        print(len(os.listdir(r"out")),"images extracted in 'out' folder")
        # print(f"Paragraph: {level2_results2[0]}")
        # print(f"Web Scrape: {level2_results3[0]}")

    title_para = get_titles_paras(level2_results2[0])

    # Final Notes (Includes Web Scraping) 
    add_picture(url,level2_results3[0])
    print("Brevis-Notes Generated.")


    finish = time.perf_counter()

    print(f'Parallel: Finished in {round(finish-start, 2)} second(s)')