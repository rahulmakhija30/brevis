#!/usr/bin/env python
# coding: utf-8

# In[9]:


from youtube_transcription import youtube_transcribe
from keywords_extractor import get_keywords
from summary_generator import summary
import io

if __name__ == '__main__':
    # Transcription
    url = input("Enter the URL = ")

    number_of_transciptions,transcripts = youtube_transcribe(url)

    if number_of_transciptions:
        with io.open("transcript.txt", "w", encoding="utf-8") as f:
            text = transcripts[0]
            f.write(transcripts[0])
            print("Transcription Done!!")
    else:
        print("No Transcript Available")

    # Keywords Extractor
    keywords=get_keywords(text,15)
    print('\nKeywords:\n',keywords)

    # Summarization
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    result = summary(text,percentage)
    print('\nSummary:\n',result)


# In[ ]:




