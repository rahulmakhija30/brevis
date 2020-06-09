import nltk
nltk.download('punkt')
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer as sumytoken
from sumy.summarizers.lex_rank import LexRankSummarizer

def summary(text,percentage):
    LANGUAGE = "english"
    SENTENCES_COUNT=int((text.count(".") + text.count("?") + text.count("!"))*(percentage/100))
    parser = PlaintextParser.from_string((text), sumytoken(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer_LexRank = LexRankSummarizer(stemmer)
    summarizer_LexRank.stop_words = get_stop_words(LANGUAGE)
    res=[]
    count=0
    for sentence in summarizer_LexRank(parser.document, SENTENCES_COUNT):    
        res.append(str(sentence))
        count+=1
        if(count==4):
            res.append("\n")
            count=0
    return '\n'.join(res)


#Driver Code
if __name__ == "__main__":
    text=input("Enter text : ")
    print()
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    
    res = summary(text,percentage)
    
    print(res)


