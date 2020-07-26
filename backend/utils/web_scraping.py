#Importing Necessary Libraries
import urllib
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import wikipediaapi

#For generating a JSON file
# import json

#Scraping Google, Youtube and Wikipedia to fetch additional resources related to the topic
class Scrapper:
	def __init__(self,keywords,google_results=2,youtube_results=2,wiki_results=1):
		self.keywords = keywords
		self.google_results = google_results
		self.youtube_results = youtube_results
		self.google_result = []
		self.youtube_result = []
		#For Wikipedia
		self.wiki_wiki = wikipediaapi.Wikipedia('en')
		self.wiki_results = wiki_results
		self.wiki_result = []

	def remove_encoding(self):
		"To remove the encodings present in the scraped links"
		for i in range(0,len(self.links)):
			if(self.links[i].find("%7B")!=-1):
				self.links[i]=self.links[i].replace("%7B","{")
	  
			if(self.links[i].find("%7C")!=-1):
				self.links[i]=self.links[i].replace("%7C","|")

			if(self.links[i].find("%7D")!=-1):
				self.links[i]=self.links[i].replace("%7D","}")

			if(self.links[i].find("%7E")!=-1):
				self.links[i]=self.links[i].replace("%7E","~")

			if(self.links[i].find("%2B")!=-1):
				self.links[i]=self.links[i].replace("%2B","+")

			if(self.links[i].find("%2A")!=-1):
				self.links[i]=self.links[i].replace("%2A","*")

			if(self.links[i].find("%2C")!=-1):
				self.links[i]=self.links[i].replace("%2C",",")

			if(self.links[i].find("%2D")!=-1):
				self.links[i]=self.links[i].replace("%2D","-")

			if(self.links[i].find("%2E")!=-1):
				self.links[i]=self.links[i].replace("%2E",".")

			if(self.links[i].find("%2F")!=-1):
				self.links[i]=self.links[i].replace("%2F","/")

			if(self.links[i].find("%5B")!=-1):
				self.links[i]=self.links[i].replace("%5B","[")

			if(self.links[i].find("%5C")!=-1):
				self.links[i]=self.links[i].replace("%5C","\\")

			if(self.links[i].find("%5D")!=-1):
				self.links[i]=self.links[i].replace("%5D","]")

			if(self.links[i].find("%3A")!=-1):
				self.links[i]=self.links[i].replace("%3A",":")

			if(self.links[i].find("%3B")!=-1):
				self.links[i]=self.links[i].replace("%3B",";")

			if(self.links[i].find("%3C")!=-1):
				self.links[i]=self.links[i].replace("%3C","<")

			if(self.links[i].find("%3D")!=-1):
				self.links[i]=self.links[i].replace("%3D","=")

			if(self.links[i].find("%3E")!=-1):
				self.links[i]=self.links[i].replace("%3E",">")

			if(self.links[i].find("%3F")!=-1):
				self.links[i]=self.links[i].replace("%3F","?")

			if(self.links[i].find("%40")!=-1):
				self.links[i]=self.links[i].replace("%40","@")

	
	def google_scrapper(self,query,number_results=2):
		"Function to scrape results from Google Search"
		query = urllib.parse.quote_plus(query) # Format into URL encoding
		ua = UserAgent()
		assert isinstance(query, str) #Search term must be a string
		assert isinstance(number_results, int) #Number of results must be an integer
		escaped_search_term = query.replace(' ', '+')
		google_url = "https://www.google.com/search?q={}&num={}".format(query,1)
		response = requests.get(google_url, {"User-Agent": ua.random})
		soup = BeautifulSoup(response.text, "html.parser")
		result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
		self.links = []
		self.titles = []
		for r in result_div:
		# Checks if each element is present, else, raise exception
			try:
				link = r.find('a', href = True)
				title = r.find('div', attrs={'class':'vvjwJb'}).get_text()

				# Check to make sure everything is present before appending
				if link != '' and title != '': 
					self.links.append(link['href'])
					self.titles.append(title)
					if(len(self.links)==number_results):
						break
				# Next loop if one element is not present
			except:
				continue

		if(len(self.links)==0):
			return 
		else:
			self.links= self.clean_results(self.links)
			self.remove_encoding()
			for i in range(0,len(self.links)):
				d=dict()
				d["title"]=self.titles[i]
				d["linktopage"]=self.links[i]
				self.google_result.append(d)

	
	def youtube_scrapper(self,query,number_results=2):
		"Function to scrape results from Youtube Search"
		query = urllib.parse.quote_plus(query) # Format into URL encoding
		ua = UserAgent()
		assert isinstance(query, str) #Search term must be a string
		assert isinstance(number_results, int) #Number of results must be an integer
		escaped_search_term = query.replace(' ', '+')
		google_url = "https://www.google.com/search?q={}&num={}".format(query+"+site:youtube.com",1)
		#print(google_url)
		response = requests.get(google_url, {"User-Agent": ua.random})
		soup = BeautifulSoup(response.text, "html.parser")
		result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
		self.Links = []
		self.Titles = []
		for r in result_div:
		# Checks if each element is present, else, raise exception
			try:
				link = r.find('a', href = True)
				title = r.find('div', attrs={'class':'vvjwJb'}).get_text()

				# Check to make sure everything is present before appending
				if link != '' and title != '': 
					self.Links.append(link['href'])
					self.Titles.append(title)
					if(len(self.Links)==number_results):
  						break
			# Next loop if one element is not present
			except:
				continue

		for i in range(0,len(self.Links)):
			self.Links[i]=self.Links[i].replace("/url?q=","")
		for i in range(0,len(self.Links)):
			if(self.Links[i].find("watch")!=-1):
				self.Links[i]=self.Links[i].replace("%3F","?")
				self.Links[i]=self.Links[i].replace("%3D","=")
				self.Links[i]=self.Links[i].split("&")[0]
			else:
				continue
		if(len(self.Links)==0):
			return
		else:
			for i in range(0,len(self.Links)):
				d=dict()
				d["title"]=self.Titles[i]
				d["linktopage"]=self.Links[i]
				self.youtube_result.append(d)

	def clean_results(self,links):
		"Cleaning the fetched links by removing unnecessary text"
		clean_links = []
		for i, l in enumerate(links):
			clean = re.search('\/url\?q\=(.*)\&sa',l)

			# Anything that doesn't fit the above pattern will be removed
			if clean is None:
				continue
			clean_links.append(clean.group(1))
		return clean_links

	def remove_sequence(self,summary):
		summary = summary.replace("\n","")
		summary = summary.replace("\\"," ")
		return summary

	def wiki_summary(self):
		"Fetching summary from Wikipedia to be displayed on the front end"
		for word in self.keywords:
			page_py = self.wiki_wiki.page(word)
			if page_py.exists() == True:#Checking if the page exists
				res={}
				res["title"]=page_py.title
				res["definition"]= self.remove_sequence(page_py.summary)
				self.wiki_result.append(res)
			else: #If the page does not exists then search result for next keyword
				continue
				#res["Not Found"]="Page for the entered query does not exists." 
			if(len(self.wiki_result) == self.wiki_results):
				break

	def web_scrape(self):
		"Scraping results by calling both scrappers and creating a JSON to be displayed"
		#Google
		for w in self.keywords:
			self.google_scrapper(w,self.google_results-len(self.google_result))
			if(len(self.google_result)== self.google_results):
				break
		#Youtube
		for w in self.keywords:
			self.youtube_scrapper(w,self.youtube_results-len(self.youtube_result))
			if(len(self.youtube_result)== self.youtube_results):
				break

		#Wikipedia
		self.wiki_summary()

		self.scrape_result=dict()
		self.scrape_result["google"]= self.google_result
		self.scrape_result["youtube"]= self.youtube_result
		self.scrape_result["wikipedia"]= self.wiki_result

		return self.scrape_result

#Driver Code
if __name__ == "__main__":
	scraped_results = Scrapper(["Artificial Intelligence","Machine Learning","Dynamic Programming"],2,2,2)
	s = scraped_results.web_scrape()
	print(s)
	# out_file=open("scrape_results.json","w")
	# json.dump(scraped_results.scrape_result,out_file,indent=4)
	# out_file.close()
