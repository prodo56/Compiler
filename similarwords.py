from iertools import chain
synonyms = wordnet.synsets(text)
lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))