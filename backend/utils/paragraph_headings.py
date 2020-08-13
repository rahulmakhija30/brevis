'''
Input : text
Output : List of tuples [(heading1,para1),...]

Paragraph Threshold:
similarity_threshold = Degree of similarity between two sentences (paragraph function)
word_threshold = Number of words in a paragraph (paragraph function)
sentence_threshold = Number of sentences in a paragraph (get_titles_paras function)
training = PASSES
heading_threshold = NUM_HEADING
percent_reduce = When sentence similarity is greater than 0.9, reduce to 0.35
Defaults : similarity_threshold=0.35, word_threshold = 20, sentence_threshold = 5, training = 500, heading_threshold = 3. percent_reduce = 0.6


Heading Threshold:
PASSES = Number of iterations to train the model
NUM_HEADING = Number of headings required
POS = List of part of speech in a priority order

Defaults : PASSES = 500, NUM_HEADING = 3, POS = ['PROPN','NOUN','VERB']
''' 
# Paragraph Imports
from gensim.models.wrappers import FastText
from gensim.models import FastText
from fse.models import Average
from fse import IndexedList
import pysbd
import re

# Heading Import Modified
from keywords_extractor import *

'''
# Heading Import
import spacy
import spacy.cli
spacy.cli.download('en_core_web_sm')
nlp = spacy.load('en_core_web_sm')

import neuralcoref
neuralcoref.add_to_pipe(nlp)

import re
import nltk
import string
import itertools

nltk.download('punkt')
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

from gensim import corpora
from gensim import models
'''

# Others
import math
import numpy as np
import os
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

	
	def sentence_similarity(self,los,percent = 0.6):
		sentences = [self.modify(i) for i in los]
		ft = FastText(sentences, min_count=1,size=12,workers=4)

		model = Average(ft)
		model.train(IndexedList(sentences),update=True,report_delay=10,queue_factor=4)

		res_similar = []
		for i in range(len(los)-1):
			res_similar.append(model.sv.similarity(i,i+1))
			
		if np.mean(res_similar) > 0.9:
			PERCENT_REDUCE = percent        
			for i in range(len(res_similar)):
				res_similar[i] -= (PERCENT_REDUCE * res_similar[i])

		return res_similar

	
	def paragraph(self,similarity_threshold=0.35, word_threshold = 20, percent_reduce = 0.6):
		# Sentence Boundary Detection
		seg = pysbd.Segmenter(language="en", clean=True)
		sentences = seg.segment(self.text) # List of sentences as string
		# print("Number of sentences : ",len(sentences))
		# Sentence Similarity
		res_similar = self.sentence_similarity(sentences,percent=percent_reduce)

		para = ''
		n = len(res_similar)
		second = sentences[0]
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

	
	def coreference(self,text):
		doc = nlp(text)
		if doc._.has_coref:
			print("Coreferencing")
			text = doc._.coref_resolved
		else:
			print("No coref")
		return text


	def process_text(self,text):
		# Make all the strings lowercase and remove non alphabetic characters
		text = re.sub('[^A-Za-z]', ' ', text.lower())

		# Tokenize the text; this is, separate every sentence into a list of words
		# Since the text is already split into sentences you don't have to call sent_tokenize
		tokenized_text = word_tokenize(text)

		# Remove the stopwords and stem each word to its root

		clean_text = [
			# lemmatizer.lemmatize(word) for word in tokenized_text
			stemmer.stem(word) for word in tokenized_text
			if word not in stopwords.words('english')
		]

		# Remember, this final output is a list of words
		return clean_text


	def spellcheck(self,text,paragraph):
		paragraph = paragraph.lower()
		heading = paragraph[paragraph.find(text):].split()[0].capitalize()
		heading = heading.translate(str.maketrans('', '', string.punctuation)).strip()
		return heading
	
	
	def GetHeadings(self,text):
		keywords = KeywordsExtractor(text).ExtractScrapeKeywords()
		if(len(keywords)==0):
			return ""
		for word in keywords:
			if word not in self.headings:
				self.headings.append(word)
				return word
		return ""



	def generate_title(self,para, PASSES = 500, NUM_HEADING = 3, POS = ['PROPN','NOUN','VERB']):
		texts = self.coreference(para).split()

		texts = [self.process_text(text) for text in texts]
		dictionary = corpora.Dictionary(texts)
		corpus = [dictionary.doc2bow(text) for text in texts]


		model = models.ldamodel.LdaModel(corpus, num_topics=1, id2word=dictionary, passes=PASSES, per_word_topics=True)

		topics = model.print_topics(num_words=NUM_HEADING)
		topic = topics[0]

		h = []
		for i in range(NUM_HEADING):
			h.append(self.spellcheck(topic[-1].split('+')[i].split("*")[-1].split("\"")[1],para))

		print(topic)


		heading_string = " ".join(h)
		doc = nlp(heading_string)
		pos_heading = {}
		for token in doc:
			if token.pos_ not in pos_heading:
				pos_heading[token.pos_] = [token.text]
			else:
				pos_heading[token.pos_].append(token.text)
		print(pos_heading)


		heading_keys = list(pos_heading.keys())
		heading_list = [pos_heading[k] for k in POS if k in heading_keys]
		headings = list(itertools.chain(*heading_list))

		print(headings[:NUM_HEADING])
			
		return headings[0]     
	

class ParaHeadings(ParaFormation):
	def __init__(self,list_para):
		self.list_para = list_para
		self.headings = []        
	
	# def get_titles_paras(self,sentence_threshold = 5, training = 200, heading_threshold = 3):
	def get_titles_paras(self,sentence_threshold = 5):
		no_of_para = len(self.list_para)
		seg = pysbd.Segmenter(language="en", clean=True)
		sent = seg.segment(' '.join(self.list_para)) # List of sentences as string
		no_of_sent = len(sent)

		print("\nNumber of paragraphs : ",no_of_para)
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
				# heading = self.generate_title(in_para,PASSES = training, NUM_HEADING = heading_threshold).strip().upper()
				heading = self.GetHeadings(in_para).strip().upper()                
				if heading != '':
					title.append((heading,in_para))
				in_para = ''

			i+=1

		if in_para != '':
			# print(len(res))
			# heading = self.generate_title(in_para,PASSES = training, NUM_HEADING = heading_threshold).strip().upper()
			heading = self.GetHeadings(in_para).strip().upper()
			title.append((heading,in_para))
				
		with open(os.path.join('res',"paragraph_headings.txt"),"w",encoding="utf-8") as f:
			num=1
			for i,j in title:
				f.write(str(num)+ ".) " + i + " $ " + j.strip() + "\n")
				num+=1

		return title

if __name__ == '__main__':
	text = input("Enter transcript : ")
	pf = ParaFormation(text)
	list_para = pf.paragraph(similarity_threshold=0.35,word_threshold = 20,percent_reduce=0.56)
	print(f"Number of paragraphs = {len(list_para)}")
	
	ph = ParaHeadings(list_para)
	# title_para = ph.get_titles_paras(sentence_threshold=2,training = 200, heading_threshold = 3)
	title_para = ph.get_titles_paras(sentence_threshold=2)
	print(title_para)
