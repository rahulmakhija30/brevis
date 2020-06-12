#Importing Libraries
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

#Function to scrape results from Google Search
def youtube_scrapper(query,youtube_result,number_results=2):
  query = urllib.parse.quote_plus(query) # Format into URL encoding
  ua = UserAgent()
  assert isinstance(query, str) #Search term must be a string
  assert isinstance(number_results, int) #Number of results must be an integer
  escaped_search_term = query.replace(' ', '+')
  google_url = "https://www.google.com/search?q={}&num={}".format(query+"+site:youtube.com",number_results+1)
  response = requests.get(google_url, {"User-Agent": ua.random})
  soup = BeautifulSoup(response.text, "html.parser")
  result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
  links = []
  titles = []
  for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href = True)
        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
        
        # Check to make sure everything is present before appending
        if link != '' and title != '': 
            links.append(link['href'])
            titles.append(title)
            if(len(links)==number_results):
              break
    # Next loop if one element is not present
    except:
        continue
  for i in range(0,number_results):
    links[i]=links[i].replace("/url?q=","")
  for i in range(0,number_results):
    if(links[i].find("watch")!=-1):
      links[i]=links[i].replace("%3F","?")
      links[i]=links[i].replace("%3D","=")
    else:
      continue
  for i in range(0,number_results):
    d=dict()
    d["title"]=titles[i]
    d["linktopage"]=links[i]
    youtube_result.append(d)


#Driver Code
if __name__=="__main__":
  query=input("Enter Query : ")
  number_results=int(input("Enter number of results to be fetched : "))
  res=[]
  youtube_scrapper(query,res,number_results)
  print(res)
