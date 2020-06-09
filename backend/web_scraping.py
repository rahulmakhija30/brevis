#Call this function to scrape results from sources and save it to json file
import json
from google_scrape import google_scrapper
from youtube_scrape import youtube_scrapper
def web_scrape(keywords,google_res=3,youtube_res=3):
  google_result={}
  youtube_result={}
  for w in keywords:
    google_result[w]=google_scrapper(w,google_res)
    youtube_result[w]=youtube_scrapper(w,youtube_res)
  #return google_result,youtube_result
  write_json(google_result,youtube_result)

def write_json(google_result,youtube_result):
    #For Google results
    out_file_google=open("google_results.json","w")
    json.dump(google_result,out_file_google,indent=4)
    out_file_google.close()
    #For Youtube Results
    out_file_youtube=open("youtube_results.json","w")
    json.dump(youtube_result,out_file_youtube,indent=4)
    out_file_youtube.close()

##if __name__== "__main__":
##    keywords=["Artificial Intelligence","Machine Learning"]
##    web_scrape(keywords)


