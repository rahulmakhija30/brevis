import spacy
nlp=spacy.load("en_core_web_lg")
from string import punctuation

def generate_vocubulary(text,doc):
    word_freq={}
    for token in doc:
        token=token.text
        token=token.strip(" ")
        token=token.lower()
        if token in nlp.Defaults.stop_words or token in punctuation or token=="\n":
            continue
        else:
            if token in word_freq:
                word_freq[token]+=1
            else:
                word_freq[token]=1
    return word_freq
	
def calc_term_freq(word_freq):
    max_frequency=max(word_freq.values())
    for key in word_freq:
        word_freq[key]/=max_frequency;
    return word_freq
	
def calc_sent_strength(word_freq,doc):
    sent_weight={}
    for sent in doc.sents:
        for word in sent:
            word=word.text
            word=word.strip(" ")
            word=word.lower()
            if(word in word_freq):
                if(sent in sent_weight):
                    sent_weight[sent]+=word_freq[word]
                else:
                    sent_weight[sent]=word_freq[word]
    return sent_weight
	
def generate_summary(sent_weight,percentage):
    top_sentences=sorted(sent_weight.values(),reverse=True)
    top_percent=int((percentage/100)*len(top_sentences))
    top_sent_final=top_sentences[:top_percent]
    summary=[]
    for sent,weight in sent_weight.items():
        if weight in top_sent_final:
            summary.append(sent)
    return summary
	
def display_summary(summary):
    if len(summary)==0:
        print("Summary is empty.Please enter a higher percentage for summary.")
    else:
        for line in summary:
            print(line,end="")

#Driver Code
if __name__=="__main__":
    text=input("Enter text : ")
    print()
    percentage=int(input("Enter the percentage of information in text you want as summary : "))
    doc=nlp(text)
    m=generate_vocubulary(text,doc)
    freq_terms=calc_term_freq(m)
    sent_strength=calc_sent_strength(freq_terms,doc)
    summary=generate_summary(sent_strength,percentage)
    print()
    display_summary(summary)
