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
import tensorflow_hub as hub

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)

if __name__ == '__main__':
    
    # Transcription and Cleaning
    url = input("Enter the URL = ")
    text = youtube_transcribe(url)
    
    # Keywords Extractor
    keywords=get_keywords(text,15)
    print('\nKeywords:\n',keywords)

    # Summarization
    # percentage=int(input("Enter the percentage of information in text you want as summary : "))
    result = summary(text,40)
    print('\nSummary:\n',result)
    
    # Keyframe Extraction (Output : 'out' folder)
    Image_Processing(url,keywords)
    print(len(os.listdir(r"out")),"images extracted in 'out' folder")
    
    # Paragraph and Headings (Output : paragraph_headings.txt)
    print("Generating Paragraphs and Headings")
    list_para = paragraph(text,model)
    title_para = get_titles_paras(list_para)
    
    # Final Notes (Includes Web Scraping) 
    s=web_scrape(keywords)
    add_picture(url,s)
    print("Brevis-Notes Generated. Also delete video.mp4 if not required.")