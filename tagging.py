import nltk
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary
#from iertools import chain
dictionary=PyDictionary()
text = nltk.word_tokenize("instantiate variable")
tags= nltk.pos_tag(text)
words=[]
for word in tags:
	if word[1] == 'NN' and len(word[0])>1:
		words.append(word[0])
		print dictionary.synonym(word[0])
		print word

'''
synonyms = wordnet.synsets(text)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
wn.synsets('make', pos='v')'''