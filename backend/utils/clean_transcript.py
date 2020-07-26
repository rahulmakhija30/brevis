#Importing necessary modules
from punctuator import Punctuator
import language_tool_python
from sys import exit
#loading model for add_punctuations function(To be loaded at the start of server)
try:
	punct_model = Punctuator('Demo-Europarl-EN.pcl')
except Exception as e:
	print()
	print("Model required for punctuation does not exists.Please download the model \"Demo-Europarl-EN.pcl\" from https://drive.google.com/drive/folders/0B7BsN5f2F1fZQnFsbzJ3TWxxMms and place it in this folder.")
	exit(0)

#loading model for correct_mistakes function(To be loaded at the start of server) 
lang_model = language_tool_python.LanguageTool('en-US')

class CleanTranscript:
	"Adding punctuation marks to the transcript and correcting grammatical mistakes"
	
	def __init__(self,text):
		self.text=text

	#Function to add proper punctuations to transcript
	def add_punctuations(self,punct_model):
		print("Adding punctuations to transcript...")
		self.text=punct_model.punctuate(self.text)

	#Function to correct spelling and grammatical errors in transcripts
	def correct_mistakes(self,lang_model):
		print("Correcting mistakes in the transcript...")
		self.matches = lang_model.check(self.text)
		self.text = lang_model.correct(self.text)

#Driver Code
if(__name__=="__main__"):
	text=input("Enter text : ")
	clean_trans=CleanTranscript(text)
	clean_trans.add_punctuations(punct_model)
	clean_trans.correct_mistakes(lang_model)
	print("Corrected Text : ")
	print()
	print(clean_trans.text)