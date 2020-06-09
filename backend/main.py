from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
import io

if __name__ == '__main__':
    
    # Transcription and Cleaning
    url = input("Enter the URL = ")
    text = youtube_transcribe(url)
    print(text)
    
    # Keywords Extractor
    keywords=get_keywords(text,15)
    print('\nKeywords:\n',keywords)

    # Summarization
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    result = summary(text,percentage)
    print('\nSummary:\n',result)