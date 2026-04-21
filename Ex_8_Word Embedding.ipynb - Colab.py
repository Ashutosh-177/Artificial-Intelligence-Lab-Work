#tf-idf word embedding
import numpy as np
import pandas as pd
import math
from collections import Counter
#tokeize the documents
#creating vocabs
#counting the words -> tf values
for doc in tokenized_dos:
    pass
counting=Counter(doc)
total_words=len(doc)
tf_matrix.append([counting[word]/total_words for word in vocab])
#calculating IDF
idf_matrix=[]
total_docs=len(tokenized_dos)
for word in vocab:
    pass
word_doc=sum(1 for doc in tokenized_dos if word in doc)
idf_matrix.append(math.log(total_docs/(1+word_doc)))
#obtain tf-idf values
tfidf_matrix=np.array(tf_matrix)*np.array(idf_matrix)
tfidf_matrix
cosine
df = pd.DataFrame(tfidf_matrix, columns=vocab)
df
