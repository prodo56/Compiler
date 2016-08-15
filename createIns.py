import nltk

def createInstruction(tag,sentence):
	#print sentence,tag
	if tag=="create":
		ins=getCreateIns(sentence)
	elif tag=="display":
		ins=getDisplayIns(sentence)
	elif tag=="assign":
		ins=getAssignIns(sentence)
	elif tag=="add":
		ins=getAddIns(sentence)
	return ins

def getCreateIns(sentence):
	ins=""
	tokens=nltk.word_tokenize(sentence)
	variable_type=""
	ins_Assigned=False
	stopwords=["create","variable"]
	datatypes=["int","string","boolean","list"]
	'''variable=''''''"predefined"
				for i in range(0,len(tokens)):
						#print tokens[i]
					if tokens[i]=="variable":
						variable_mentioned=True
						try:
							variable=tokens[i+1]
							break
						except Exception, e:
							break
					elif len(tokens[i])==1:
						variable=tokens[i]'''
	#print variable
	#if variable_mentioned:
	variable=getVariable(datatypes,tokens)
	tokens=[x for x in tokens if x not in stopwords and len(x)>1]
	for token in tokens:
		if token.lower() in datatypes:
			variable_type=token
			ins=token+" ?"
			ins_Assigned=True
	if not ins_Assigned:
		ins = "string ?"
	ins=ins.replace("?",variable)
	ins=ins+";"
	return ins

def getVariable(datatypes,tokens):
	stopwords=["create"]+datatypes
	tokens=[x for x in tokens if x not in stopwords]
	print tokens
	variable_name="predefined"
	variable_mentioned=False
	if(len(tokens)==1):
		variable_name=tokens[0]
	else:
		for i in range(0,len(tokens)):
			#print tokens[i]
			if tokens[i]=="variable":
				variable_mentioned=True
				try:
					variable_name=tokens[i+1]
					break
				except Exception, e:
					break
			elif len(tokens[i])==1:
				variable_name=tokens[i]
	return variable_name

def getDisplayIns(sentence):
	ins="print ?"
	tokens=nltk.word_tokenize(sentence)
	variable_name="predefined"
	for i in range(0,len(tokens)):
			#print tokens[i]
		if tokens[i]=="variable":
			variable_mentioned=True
			try:
				variable_name=tokens[i+1]
				break
			except Exception, e:
				break
		elif len(tokens[i])==1:
			variable_name=tokens[i]
	ins=ins.replace("?",variable_name)
	return ins+";"

def getAssignIns(sentence):
	#ins=""
	tokens=nltk.word_tokenize(sentence)
	tagged=nltk.pos_tag(tokens)
	value,variable=findVariableAndValue(tagged,tokens,sentence)
	ins=variable+"="+value
	return ins+";"

def findVariableAndValue(tagged,tokens,sentence):
	value=""
	tag=["CD","TO"]
	variable_name="predefined"
	quote_count=[i for i,letter in enumerate(sentence) if letter=="\'"]
	if len(quote_count)>=2 and len(quote_count)%2==0:
		value="'"+sentence[quote_count[0]+1:quote_count[1]]+"'"
	i=0
	for tags in tagged:
		if tags[1] in tag:
			if tags[1]=="CD":
				value=tags[0]
			elif tags[1]=="TO":
				variable=tokens[i+1]
				break
		i=i+1
	return value,variable

def getAddIns(sentence):
	values=[]
	stopwords=["add","sum","total","tally","append","concatinate"]
	tokens=nltk.word_tokenize(sentence)
	tokens=[x for x in tokens if x not in stopwords]
	tagged=nltk.pos_tag(tokens)
	new_tokens=[]
	ins="0"
	for (x,y) in tagged:
		if y in ["NN","CC","CD","TO","VB"]:
			new_tokens.append((x,y))
	for (x,y) in new_tokens:
		if y!="CC" and y!="TO":
			values.append(x)
			ins=ins+"+"+x+"+"
	return ins[0:len(ins)-1].replace("++","+")