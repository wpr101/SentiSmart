import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()
docs = np.array([
	'The sun is shining',
	'The weather is sweet',
	'The sun is shining and the weather is sweet'
	])
bag = count.fit_transform(docs)
print(count.vocabulary_)
print(bag.toarray())