from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
from clean_transcript import add_punctuations,correct_mistakes
import io

if __name__ == '__main__':
    # Transcription and Cleaning
    url = input("Enter the URL = ")

    number_of_transciptions,transcripts = youtube_transcribe(url)

    if number_of_transciptions:
        with open("transcript.txt","w") as f:
                while number_of_transciptions > 0:
                    if '.' in transcripts[number_of_transciptions-1]:
                        text = transcripts[number_of_transciptions-1]
                        f.write(transcripts[number_of_transciptions-1])
                        break
                
                    if number_of_transciptions == 1:
                        text = transcripts[0]
                        text=add_punctuations(text,punct_model)
                        text=correct_mistakes(text,lang_model)
                        f.write(transcripts[0])
                        
                    number_of_transciptions-=1
                    
        print("Transcription and Cleaing Done!!")
    else:
        print("No Transcript Available")
    
    print(text)
    
    # Keywords Extractor
    keywords=get_keywords(text,15)
    print('\nKeywords:\n',keywords)

    # Summarization
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    result = summary(text,percentage)
    print('\nSummary:\n',result)