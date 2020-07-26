#Importing required modules
import RAKE
import operator
from sys import exit
class KeywordsExtractor:
    def __init__(self,text,num_keywords):
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
        if(self.num_keywords > len(self.keywords)):
            print("No. of keywords entered by the user is more than the number of keywords generated.")
            exit(1)
        self.keywords=self.keywords[:self.num_keywords]
        return self.keywords

    
if __name__ == "__main__":
	text=input("Enter text : ")
	num_keywords=int(input("Enter number of keywords to be extracted : "))
	words=KeywordsExtractor(text,num_keywords)
	keywords = words.ExtractKeywords()
	print("Keywords : ",keywords)