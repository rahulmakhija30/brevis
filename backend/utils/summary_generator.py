#Importing necessary Modules
import nltk
nltk.download('punkt')
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer as sumytoken
from sumy.summarizers.lex_rank import LexRankSummarizer

class Summarizer:
	"Extraction of summary for a given text"
	def __init__(self):
		self.LANGUAGE = "english"
		self.stemmer = Stemmer(self.LANGUAGE)
		self.summarizer_LexRank = LexRankSummarizer(self.stemmer)
		self.summarizer_LexRank.stop_words = get_stop_words(self.LANGUAGE)

	def summary(self,text,percentage):
		self.SENTENCES_COUNT=int((text.count(".") + text.count("?") + text.count("!"))*(percentage/100))
		self.parser = PlaintextParser.from_string((text), sumytoken(self.LANGUAGE))
		self.res=[]
		for sentence in self.summarizer_LexRank(self.parser.document, self.SENTENCES_COUNT):    
			self.res.append(str(sentence))
			self.res.append(" ")
    
		self.final_summ = ''.join(self.res)
		with open("summary.txt","w",encoding="utf-8") as f:
			f.write(self.final_summ)
		f.close()    
		return self.final_summ

if __name__=="__main__":
	summ = Summarizer()
	text=input("Enter text : ")
	print()
	percentage=int(input("Enter percentage of text you want as summary : "))
	print()
	print("Summary :-")
	print()
	print(summ.summary(text,percentage))