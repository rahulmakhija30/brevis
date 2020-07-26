'''
Input : text
Output : List of tuples [(heading1,para1),...]

Threshold:
Similarity_threshold = Degree of similarity between two sentences (paragraph function)
Word_threshold = Number of words in a paragraph (paragraph function)
Sentence_threshold = Number of sentences in a paragraph (get_titles_paras function)
''' 

from collections import Counter
import pysbd
import spacy
import neuralcoref
import spacy.cli

import math
import numpy as np
import os

spacy.cli.download('en_core_web_lg')
nlp = spacy.load('en_core_web_lg')
neuralcoref.add_to_pipe(nlp)

from gensim.models.wrappers import FastText
from gensim.models import FastText
import re
from fse.models import Average
from fse import IndexedList
import time
import logging

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',level=logging.INFO)

import warnings
warnings.filterwarnings("ignore")

class ParaFormation:
    def __init__(self,text):
        self.text = text

    def modify(self,string):
        return re.sub('[^A-Za-z0-9]+', ' ', string).strip().lower().split()

    def sentence_similarity(self,los):
        sentences = [self.modify(i) for i in los]
        ft = FastText(sentences, min_count=1,size=12,workers=4)

        model = Average(ft)
        model.train(IndexedList(sentences),update=True,report_delay=10,queue_factor=4)

        res_similar = []
        for i in range(len(los)-1):
            res_similar.append(model.sv.similarity(i,i+1))

        return res_similar

    def paragraph(self,similarity_threshold=0.35,word_threshold = 20):
        # Sentence Boundary Detection
        seg = pysbd.Segmenter(language="en", clean=True)
        sentences = seg.segment(self.text) # List of sentences as string
        # print("Number of sentences : ",len(res))

        # Sentence Similarity
        res_similar = self.sentence_similarity(sentences)

        para = ''
        n = len(res_similar)
        for i in range(n-1):
            first = sentences[i]
            second = sentences[i+1]
            similar = res_similar[i]
            similar = round(similar,2)
            # print("Sentence ",i,',',i+1," : ",similar)

            if similar < 0: 
                continue

            if similar >= similarity_threshold:
                para += first.strip() + ' '

            else:
                para += first.strip() + '\n'

        para += second.strip()        

        # Merge Small Sentences with the previous para
        p = para.split('\n')
        final = ''
        for i in range(1,len(p)):
            small = len(p[i-1].split(' '))

            if small >= word_threshold:
                final += p[i-1] + '\n'

            else:
                final += p[i-1] + ' '

        final += p[len(p)-1]

        return final.split('\n')    # List of paragraphs

    def generate_title(self,i):
        string=""
        isfound=False
        doc = nlp(i)
        nlp.remove_pipe("neuralcoref")
        coref = neuralcoref.NeuralCoref(nlp.vocab)
        nlp.add_pipe(coref, name='neuralcoref')

        #remove stopwords and punctuations
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        Nouns = [chunk.text for chunk in doc.noun_chunks]
        Adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"]
        word_freq = Counter(words)
        word_freqNoun = Counter(Nouns)
        word_freqADJ = Counter(Adjectives)
        common_words = word_freq.most_common(5)
        common_wordsNoun = word_freqNoun.most_common(10)
        common_wordsADJ = word_freqADJ.most_common(10)
        maxcount = common_words[0][1]
        Range = min(len(common_wordsNoun),len(common_wordsADJ))
        title2 = ''
        title1 = ''
        for j in range(Range):
            title2 = common_wordsADJ[j][0]+" "+common_wordsNoun[j][0]
            if title2 in i:
                # print("Adjective + Noun Title : ",title2)
                break

        for j in common_words:
            if j[1]==maxcount:
                string+=j[0]+" "
        string = string[:-1]
        while not isfound:
            if string in i:
                isfound = True
                title1 = string
                # print("Title : ",title1)
            else :
                string = ' '.join(string.split(' ')[:-1])
        title = [common_wordsNoun[0][0]]
        title = ' '.join(title)
        # print("Noun Title : ",title)

        #title - phrases
        #title1 - single word
        #title2 - adj + noun title

        if len(title) >= 5 and title != '' : 
            return title

        elif len(title1) >= 5 and title1 != '':
            return title1

        elif len(title2) >= 5 and title2 != '':
            return title2

        else:
            return ''

class ParaHeadings(ParaFormation):
    def __init__(self,list_para):
        self.list_para = list_para
        
    def get_titles_paras(self,sentence_threshold = 5):
        no_of_para = len(self.list_para)
        seg = pysbd.Segmenter(language="en", clean=True)
        sent = seg.segment(' '.join(self.list_para)) # List of sentences as string
        no_of_sent = len(sent)

        # print("\nNumber of paragraphs : ",no_of_para)
        # print("Number of sentences : ",no_of_sent)

        i=0
        in_para = ''
        title = []
        while(i<no_of_para):
            in_para = in_para + ' ' + self.list_para[i]
            seg = pysbd.Segmenter(language="en", clean=True)
            res = seg.segment(in_para) # List of sentences as string

            if len(res) >= sentence_threshold:
                # print(len(res))
                heading = self.generate_title(in_para).strip().upper()
                if heading != '':
                    title.append((heading,in_para))
                in_para = ''

            i+=1

        if in_para != '':
            # print(len(res))
            heading = self.generate_title(in_para).strip().upper()
            title.append((heading,in_para))

        with open("paragraph_headings.txt","w",encoding="utf-8") as f:
            for i,j in title:
                f.write(i + " $ " + j.strip() + "\n")

        return title

if __name__ == '__main__':
    text = input("Enter transcript : ")
    pf = ParaFormation(text)
    list_para = pf.paragraph()
    # print(list_para)
    
    ph = ParaHeadings(list_para)
    title_para = ph.get_titles_paras(sentence_threshold=2)
    print(title_para)
