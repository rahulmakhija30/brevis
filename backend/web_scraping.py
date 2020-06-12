#Call this function to scrape results from sources and save it to json file
import json
from google_scrape import google_scrapper
from youtube_scrape import youtube_scrapper
def web_scrape(keywords,google_res=2,youtube_res=2):
  google_result=[]
  youtube_result=[]
  for w in keywords:
    google_scrapper(w,google_result,google_res-len(google_result))
    if(len(google_result)==google_res):
      break
    
  for w in keywords:
    youtube_scrapper(w,youtube_result,youtube_res-len(youtube_result))
    if(len(youtube_result)==youtube_res):
      break

  scrape_result=dict()
  scrape_result["google"]=google_result
  scrape_result["youtube"]=youtube_result
  return scrape_result

def write_json(scrape_result):
    #For Scrape results
    out_file=open("scrape_results.json","w")
    json.dump(scrape_result,out_file,indent=4)
    out_file.close()

if __name__== "__main__":
    keywords=["wonky equals signor","machine learning"]
    res=web_scrape(keywords)
    print(res)
