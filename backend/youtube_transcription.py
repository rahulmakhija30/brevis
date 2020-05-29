# Import Modules
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup as bs
from urllib import parse

# Function to get details about a video
def get_video_info(url):
    # download HTML code
    content = requests.get(url)
    # create beautiful soup object to parse HTML
    soup = bs(content.content, "html.parser")
    # initialize the result
    result = {}
    # video title
    result['title'] = soup.find("span", attrs={"class": "watch-title"}).text.strip()
     # video views (converted to integer)
    result['views'] = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))
    # video description
    result['description'] = soup.find("p", attrs={"id": "eow-description"}).text
    # date published
    result['date_published'] = soup.find("strong", attrs={"class": "watch-time-text"}).text
     # number of likes as integer
    result['likes'] = int(soup.find("button", attrs={"title": "I like this"}).text.replace(",", ""))
    # number of dislikes as integer
    result['dislikes'] = int(soup.find("button", attrs={"title": "I dislike this"}).text.replace(",", ""))
     # channel details
    channel_tag = soup.find("div", attrs={"class": "yt-user-info"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str
    channel_subscribers = soup.find("span", attrs={"class": "yt-subscriber-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    # return the result
    
    res = (f"Title: {data['title']}" + '\n'
           f"Views: {data['views']}" + '\n'
           f"\nDescription: {data['description']}\n" + '\n'
           f"{data['date_published']}" + '\n'
           f"Likes: {data['likes']}" + '\n'
           f"Dislikes: {data['dislikes']}" + '\n'
           f"\nChannel Name: {data['channel']['name']}" + '\n'
           f"Channel URL: {data['channel']['url']}" + '\n'
           f"Channel Subscribers: {data['channel']['subscribers']}" + '\n')

    return result,res.strip()

# If you want to print individual fields, uncomment them

# data,res = get_video_info(url)
# print(f"Title: {data['title']}")
# print(f"Views: {data['views']}")
# print(f"\nDescription: {data['description']}\n")
# print(data['date_published'])
# print(f"Likes: {data['likes']}")
# print(f"Dislikes: {data['dislikes']}")
# print(f"\nChannel Name: {data['channel']['name']}")
# print(f"Channel URL: {data['channel']['url']}")
# print(f"Channel Subscribers: {data['channel']['subscribers']}")

# No transcript - https://www.youtube.com/watch?v=Bv_5Zv5c-Ts&t=1836s

'''
  Function youtube_transcribe
  Input : url, optional arg -> descp 
          decsp : Provides description of YouTube Video : bool
  Output : number of transcriptions available and transcriptions
'''

def youtube_transcribe(url,descp=False):
  try:
    parse.urlsplit(url)
    parse.parse_qs(parse.urlsplit(url).query)
    url_id = dict(parse.parse_qsl(parse.urlsplit(url).query))['v']

    available_transcript = list(YouTubeTranscriptApi.list_transcripts(url_id))

    transcript = []
    for i in available_transcript:
      if i.language_code == 'en':
        res = ''
        for j in i.fetch():
          res = res + j['text'] +' '
        transcript.append(res)

    if(descp):
      data,res = get_video_info(url)
      print("Video Description:\n\n",res)
    
    return len(transcript),transcript

  except:
    return 0,[0]

if __name__ == '__main__':
  url = input("Enter the URL = ")

  number_of_transciptions,transcripts = youtube_transcribe(url)

  # print('\nNumber of transcript =',number_of_transciptions)

  # for i in range(number_of_transciptions):
  #   print('\nTranscript Number =',i+1,'\n\n',transcripts[i],'\n\n')

  if number_of_transciptions:
    with open("transcript.txt","w") as f:
      f.write(transcripts[-1])
      print("Transcription Done!!")
  else:
    print("No Transcript Available")

