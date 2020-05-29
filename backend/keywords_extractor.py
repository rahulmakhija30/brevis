#Loading spacy larger prediction model 
import spacy
# nlp=spacy.load('en_core_web_lg')
nlp=spacy.load('en_core_web_md')
from string import punctuation #To detect punctuation marks


#Function to generate keywords from a given text
'''
Function Name : get_keywords
Input Arguments : script : str - text to extract keywords
                  n : int - number of keywords
                  noun_chunk : bool - Noun Chunks from the text
                  pos_tag : list of pos excepted
                  dep_tag : list of dep accepted

Output : List of keywords
'''

def get_keywords(script,n=50,noun_chunk=False,pos_tag=["PROPN","ADJ","NOUN","VERBS"],dep_tag=['nsubj','pobj','compound',"pron"]):
    result={}
    doc=nlp(script.lower())
    ents=[i.text for i in doc.ents]
    
    if noun_chunk:
      c = []
      for chunk in doc.noun_chunks:
        c.append(chunk.text)
      c = list(set(c))
      print("Noun Chunks = ",c[:n])
      
    for token in doc:
        #print(token.pos_) Selecting all tokens whose pos tag is present in thr pos_tag list argument
        st=token.lemma_.strip(" ")
        if token.text in ents:    
            if st in result:
                result[st]+=1
            else:
                result[st]=1
        if token in nlp.Defaults.stop_words or token.lemma_ in punctuation:
            continue
        if(token.pos_ in pos_tag):
            if st in result:
                result[st]+=1
            else:
                result[st]=1

        if(token.dep_ in dep_tag):
            if st in result and st != '-PRON-':
                result[st]+=1
            else:
                result[st]=1

    keywords=[v[0] for v in sorted(result.items(), key=lambda items:items[1], reverse=True)]
    return keywords[:n]
    
#Driver Code
if __name__ == '__main__':
  text=input("Enter some text : ")
  print()

  keywords=get_keywords(text,15,True)

  print(keywords)

