#Importing required modules
import RAKE
import operator
import textrazor
textrazor.api_key = "0b9fcea7af6471cbae27b0a877229d23751fbfd2d4961719a3dcdad3"
from sys import exit
import os
class KeywordsExtractor:
	def __init__(self,text,num_keywords=10):
		self.text=text
		self.num_keywords=num_keywords
		
	def ExtractKeywords(self):
		"Function to extract keywords from the given text."
		self.stop_dir="SmartStoplist.txt"
		try:
			self.rake_object = RAKE.Rake(self.stop_dir)
		except Exception as e:
			print("SmartStoplist.txt file is missing.Please place the file in this folder.")
			exit(1)
		self.keywords_weighted = self.rake_object.run(self.text)
		self.keywords=list()
		for word,weight in self.keywords_weighted:
			self.keywords.append(word)

		#Handling Error
		#if(self.num_keywords > len(self.keywords)):
			#print("No. of keywords entered by the user is more than the number of keywords generated.")
			#exit(1)
		if(len(self.keywords) > self.num_keywords):
			self.keywords=self.keywords[:self.num_keywords]
		return self.keywords
		
	def ExtractScrapeKeywords(self):
		#TextRazor API Extraction
		client = textrazor.TextRazor(extractors=["entities"])
		response = client.analyze(self.text)

		entities = list(response.entities())
		entities.sort(key=lambda x: x.relevance_score, reverse=True)
		seen = set()
		self.scrape_keywords=list()
		for entity in entities:
			if entity.id not in seen:
				self.scrape_keywords.append(entity.id)
				seen.add(entity.id)
		if(len(self.scrape_keywords) > 10):
			self.scrape_keywords = self.scrape_keywords[:10]
		return self.scrape_keywords
	  
	
if __name__ == "__main__":
	text=input("Enter text : ")
	num_keywords=int(input("Enter number of keywords to be extracted : "))
	words=KeywordsExtractor(text,num_keywords)
	keywords = words.ExtractKeywords()
	scrape_keywords=words.ExtractScrapeKeywords()
	print("Keywords : ",keywords)
	print()
	print("Scrape Keywords : ",scrape_keywords)
