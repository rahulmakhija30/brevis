from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
from keyframes import Image_Processing
from text_recognition_and_extraction import text_recognition
import io

if __name__ == '__main__':
    
    # Transcription and Cleaning
    url = input("Enter the URL = ")
    text = youtube_transcribe(url)
    print('\nTranscript:\n',text)
    print(text)
    
    # Keywords Extractor
    keywords=get_keywords(text,15)
    print('\nKeywords:\n',keywords)

    # Summarization
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    result = summary(text,percentage)
    print('\nSummary:\n',result)
    
    # Keyframe Extraction
    Image_Processing(url,keywords)
    print("Images Extracted in 'out' folder")
    
    # Text Recognition And Extraction
    text_recognition()
    print("Cropped Text Extracted in 'crop' folder")