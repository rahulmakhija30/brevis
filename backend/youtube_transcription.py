# Import Modules
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptAvailable
from youtube_transcript_api._errors import TranscriptsDisabled
from youtube_transcript_api._errors import *
from requests import ConnectionError

from google_speech_to_text import speech_to_text
from urllib import parse
from clean_transcript import add_punctuations,correct_mistakes
import clean_transcript
import requests
import traceback
import re

# No transcript - https://www.youtube.com/channel/UCsFmLpSNJuFzpKqdEj5jeHw (Testing)

'''
  Function youtube_transcribe
  Input : url
  Output : transcript
'''

def youtube_transcribe(url):
    text = ''
    try:
        urlID = url.partition('https://www.youtube.com/watch?v=')[-1]

        transcript_list = YouTubeTranscriptApi.list_transcripts(urlID)

        t = list(transcript_list)

        for i in range(len(t)):
            if t[i].language_code == 'en':

                # Manually Created
                if not(t[i].is_generated):
                    print("Got Manually Created Transcript")
                    data = t[i].fetch()
                    res=''
                    for i in data:
                        res = res + ' ' + i['text']
                    
                    print("Cleaning Manually Created Transcript")
                    text = res.replace('\n',' ')
                    text = text.strip()
                    break
                    
                # Auto-generated 
                if i == len(t)-1 and t[i].is_generated:
                    print("Got Auto-generated Transcript")
                    data = t[i].fetch()
                    res=''
                    for i in data:
                        res += i['text']
                        
                    print("Cleaning Auto-generated Transcript")
                    text = res.replace('\n',' ')
                    text = add_punctuations(text,clean_transcript.punct_model)
                    text = correct_mistakes(text,clean_transcript.lang_model)
                    
        text = re.sub("[\[].*?[\]]", "", text).strip()
        
        with open("transcript.txt","w",encoding="utf-8") as f:
            f.write(text)
        
        print("Transcription and Cleaning Done!!")
        return text
        
    # No Transcript
    except NoTranscriptAvailable as t:
        print("No Transcript Available - Trying to generate one!!")
        text = speech_to_text(url)
        
    except TranscriptsDisabled as s:
        print("Subtitles are disabled for this video - Trying to generate one!!")
        text = speech_to_text(url)
        
    # Other Errors
    except VideoUnavailable as v:
        print("Video is not available")
        
    except ConnectionError as c:
        print("No Internet")
        
    except Exception as e:
        traceback.print_exc()
        print(e)
        
    finally:
        if text == '': 
            print("No Transcript")
            return ''
        
        else: return text
        

if __name__ == '__main__':
    url = input("Enter the URL = ")
    text = youtube_transcribe(url)
    print(text)