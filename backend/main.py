from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
from keyframes import Image_Processing
from paragraph_headings import paragraph,get_titles_paras
from notes import add_picture
from web_scraping import web_scrape

import notes
import io
import pytesseract

# Path to your tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'G:\himanshu\Tesseract-OCR\tesseract.exe'

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
    print("Images Extracted in 'out' folder")
    
    # Paragraph and Headings (Output : paragraph_headings.txt)
    list_para = paragraph(text)
    title_para = get_titles_paras(list_para)
    
    # Web Scraping
    
    
    # Final Notes
    s=web_scrape(["Artificial Intelligence"])
    add_picture("https://www.youtube.com/watch?v=ukzFI9rgwfU",s)