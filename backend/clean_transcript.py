from punctuator import Punctuator
import language_tool_python

#loading model for add_punctuations function(To be loaded at the start of server)
punct_model = Punctuator('Demo-Europarl-EN.pcl')

#loading model for correct_mistakes function(To be loaded at the start of server) 
lang_model = language_tool_python.LanguageTool('en-US')

#Function to add proper punctuations to transcript
def add_punctuations(text,punct_model):
  return punct_model.punctuate(text)

#Function to correct spelling and grammatical errors in transcripts
def correct_mistakes(text,lang_model):
  matches = lang_model.check(text)
  return lang_model.correct(text)

#Driver Code
if(__name__=="__main__"):
  text=input("Enter text : ")
  text=add_punctuations(text,punct_model)
  text=correct_mistakes(text,lang_model)
  print(text)