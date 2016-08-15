from nltk.corpus import wordnet
from PyDictionary import PyDictionary

def get_words(word):
	dictionary=PyDictionary()
	#print word
	syn=[j.name() for i in wordnet.synsets(word) for j in i.lemmas()]
	syn=list(set(syn))
	#print syn,word
	'''
	for w in syn:
		s=dictionary.synonym(w)
		print s,w
		if s:
			for i in s:
				words.append(i)
				#print i,w 
	#print words '''
	#words=list(set(syn))
	#print syn
	return syn