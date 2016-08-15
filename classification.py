from textblob.classifiers import NaiveBayesClassifier
import getWords as w
import nltk
from collections import Counter
import createIns as ins 
'''
train=[("create new variable", "create"),
("create new x", "create"),
("need variable x", "create"),
("want variable x", "create"),
("need new variable", "create"),
("need new variable x", "create"),
("show x", "print"),
("display variable x", "print"),
("print x", "print"),("make variable","create"),("cook x","create")]
test=["how about new variable","form variable","instantiate variable","declare x","expose x", "present x","exhibit x"]
cl = NaiveBayesClassifier(train)
for sentence in test:
	print cl.classify(sentence)
#cl.accuracy(test)
'''
def createTrainingSet(words):
	train=[]
	for word in words:
		#train.append((word,word))
		syn_list=w.get_words(word)
		if syn_list:
			for i in syn_list:
				train.append((i,word))
	return train

words=["display","create"]
#train=createTrainingSet(words)
#print train
train=[("exhibit","display"),("show","display"),("showing","display"),("expose","display"),("presentation","display"),("display","display"),("make","create"),("produce","create"),("create","create"),("put","assign"),("designate","assign"),("assign","assign"),("specify","assign"),("allot","assign"),("total","add"),("sum","add"),("append","add"),("tally","add"),("concatinate","add"),("add","add")]
classifier=NaiveBayesClassifier(train)
sentences=["create string variable x","display variable","display variable x","create variable","create string","assign 5 to x","create string random","add 5 and 6","add 5 to random"]
pos_tags=["VB","VBD","VBG","VBN","VBP","VBZ","NN","NNS","NNP","NNPS","RB","RBR","RBS"]

for sentence in sentences:
	tokens=nltk.word_tokenize(sentence)
	tagged=nltk.pos_tag(tokens)
	#print tagged
	word_list=[]
	for word in tagged:
		if word[1] in pos_tags and len(word[0])>1:
			word_list.append(classifier.classify(word[0]))
	#print word_list
	counts=dict(Counter(word_list))
	tag=counts.keys()[0]
	instruction=ins.createInstruction(tag,sentence)
	print "sentence: "+sentence+"\ninstruction: "+instruction+"\n"

