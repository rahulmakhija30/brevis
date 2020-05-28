#Loading spacy larger prediction model 
import spacy
nlp=spacy.load("en_core_web_lg")

from string import punctuation #To detect punctuation marks
#Function to generate keywords from a given text
def get_keywords(script,pos_tag=["PROPN","ADJ","NOUN","VERBS"]):
    result={}
    doc=nlp(script.lower())
    ents=[i.text for i in doc.ents]
    for token in doc:
        #print(token.pos_) Selecting all tokens whose pos tag is present in thr pos_tag list argument
        if token.text in ents:
            st=token.text
            st.strip(" ")
            if st in result:
                result[st]+=1
            else:
                result[st]=1
        if token in nlp.Defaults.stop_words or token.text in punctuation:
            continue
        if(token.pos_ in pos_tag):
            st=token.text
            st.strip(" ")
            if st in result:
                result[st]+=1
            else:
                result[st]=1
    keywords=[v[0] for v in sorted(result.items(), key=lambda items:items[1], reverse=True)]
    return keywords           

#Driver Code
text=input("Enter some text : ")
print()
keywords=get_keywords(text)
print(keywords)