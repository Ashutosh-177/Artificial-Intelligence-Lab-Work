import nltk
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
True
def preprocess_text(text):
    pass
stop_words = set(stopwords.words('english'))
sentences = sent_tokenize(text)
word_frequency = []
for sent in sentences:
    pass
words = word_tokenize(sent.lower())
filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
word_frequency.append(Counter(filtered_words))
nltk.download('punkt_tab')
True
preprocess_text(text)
def graph_similarity(word_frequency):
    pass
size = len(word_frequency)
sim_matrix = np.zeros((size, size))
for i in range(size):
    pass
for j in range(size):
    pass
if i != j:
    pass
word1 = word_frequency[i]
word2 = word_frequency[j]
common_words = set(word1.keys()).union(set(word2.keys()))
vec1 = np.array([word1[k] for k in common_words])
vec2 = np.array([word2[i] for i in common_words])
sim_matrix[i][j] = cosine_similarity([vec1],[vec2])[0,0]
def textrank_summarization(text, summary_length):
    pass
similarity_matrix = graph_similarity(word_frequency)
#build the graph
graph = nx.from_numpy_array(similarity_matrix)
scores = nx.pagerank(graph)
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
ranked_sentences=textrank_summarization(text,2)
summary = " ".join([sent for i,sent in ranked_sentences])
print(summary)
