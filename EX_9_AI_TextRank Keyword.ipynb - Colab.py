import numpy as np
import nltk
import networkx as nx
from collections import Counter
from itertools import combinations
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
True
def textrank_keywords(text, top_n):
    pass
stop_words = set(stopwords.words('english'))
words = [word.lower() for word in word_tokenize(text) if word.isalnum() and word.lower() not in stop_words]
# Create a graph using nx
graph = nx.Graph()
graph.add_nodes_from(set(words))
for w1, w2 in combinations(words, 2):
    pass
graph.add_edge(w1, w2)
scores = nx.pagerank(graph)
ranked_words = sorted(scores, key=scores.get, reverse=True)
top_keywords = ranked_words[:top_n]
keywords = textrank_keywords(text,15)
print(keywords)
keywords
