#Importing Libraries
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

#Function to scrape results from Google Search
def google_scrapper(query,number_results=3):
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
  links=clean_results(links,titles)
  return dict(zip(titles,links))

#Function to remove useless results and clean the links
def clean_results(links,titles):
  to_remove = []
  clean_links = []
  for i, l in enumerate(links):
    clean = re.search('\/url\?q\=(.*)\&sa',l)

    # Anything that doesn't fit the above pattern will be removed
    if clean is None:
        to_remove.append(i)
        continue
    clean_links.append(clean.group(1))

# Remove the corresponding titles
  for x in to_remove:
    del titles[x]
  return clean_links

#Driver Code
if __name__=="__main__":
  query=input("Enter Query : ")
  number_results=int(input("Enter number of results to be fetched : "))
  res=google_scrapper(query,number_results)
  print(res)
