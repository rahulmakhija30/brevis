#Importing Libraries
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

def remove_encoding(links):
  for i in range(0,len(links)):
    if(links[i].find("%7B")!=-1):
      links[i]=links[i].replace("%7B","{")
      
    if(links[i].find("%7C")!=-1):
      links[i]=links[i].replace("%7C","|")

    if(links[i].find("%7D")!=-1):
      links[i]=links[i].replace("%7D","}")

    if(links[i].find("%7E")!=-1):
      links[i]=links[i].replace("%7E","~")

    if(links[i].find("%2B")!=-1):
      links[i]=links[i].replace("%2B","+")
      
    if(links[i].find("%2A")!=-1):
      links[i]=links[i].replace("%2A","*")

    if(links[i].find("%2C")!=-1):
      links[i]=links[i].replace("%2C",",")

    if(links[i].find("%2D")!=-1):
      links[i]=links[i].replace("%2D","-")

    if(links[i].find("%2E")!=-1):
      links[i]=links[i].replace("%2E",".")
      
    if(links[i].find("%2F")!=-1):
      links[i]=links[i].replace("%2F","/")

    if(links[i].find("%5B")!=-1):
      links[i]=links[i].replace("%5B","[")

    if(links[i].find("%5C")!=-1):
      links[i]=links[i].replace("%5C","\\")

    if(links[i].find("%5D")!=-1):
      links[i]=links[i].replace("%5D","]")
      
    if(links[i].find("%3A")!=-1):
      links[i]=links[i].replace("%3A",":")

    if(links[i].find("%3B")!=-1):
      links[i]=links[i].replace("%3B",";")

    if(links[i].find("%3C")!=-1):
      links[i]=links[i].replace("%3C","<")

    if(links[i].find("%3D")!=-1):
      links[i]=links[i].replace("%3D","=")
      
    if(links[i].find("%3E")!=-1):
      links[i]=links[i].replace("%3E",">")

    if(links[i].find("%3F")!=-1):
      links[i]=links[i].replace("%3F","?")

    if(links[i].find("%40")!=-1):
      links[i]=links[i].replace("%40","@")
      
    

      
#Function to scrape results from Google Search
def google_scrapper(query,google_result,number_results=2):
  query = urllib.parse.quote_plus(query) # Format into URL encoding
  ua = UserAgent()
  assert isinstance(query, str) #Search term must be a string
  assert isinstance(number_results, int) #Number of results must be an integer
  escaped_search_term = query.replace(' ', '+')
  google_url = "https://www.google.com/search?q={}&num={}".format(query,number_results+1)
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
  if(len(links)==0):
    return 
  else:
    links=clean_results(links)
    #print(links)
    remove_encoding(links)
    #print(links)
    for i in range(0,len(links)):
      d=dict()
      d["title"]=titles[i]
      d["linktopage"]=links[i]
      google_result.append(d)

def clean_results(links):
  clean_links = []
  for i, l in enumerate(links):
    clean = re.search('\/url\?q\=(.*)\&sa',l)

    # Anything that doesn't fit the above pattern will be removed
    if clean is None:
        continue
    clean_links.append(clean.group(1))
    
  return clean_links

#Driver Code
if __name__=="__main__":
  query=input("Enter Query : ")
  number_results=int(input("Enter number of results to be fetched : "))
  res=[]
  google_scrapper(query,res,number_results)
  print(res)
