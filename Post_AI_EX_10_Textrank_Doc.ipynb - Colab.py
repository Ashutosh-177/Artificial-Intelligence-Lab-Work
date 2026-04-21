# Required Libraries
import nltk
import numpy as np
import networkx as nx
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')
True
# Your portfolio text
nltk.download('punkt_tab')
True
# Step 1: Sentence Tokenization
sentences = sent_tokenize(text)
# Step 2: Preprocess Sentences
stop_words = set(stopwords.words('english'))
def preprocess(sentence):
    pass
words = word_tokenize(sentence.lower())
processed_sentences = [preprocess(sentence) for sentence in sentences]
# Step 3: Create Sentence Vectors
def sentence_to_vector(words, all_words):
    pass
vector = np.zeros(len(all_words))
for word in words:
    pass
if word in all_words:
    pass
index = all_words.index(word)
# Build a vocabulary of all unique words
all_words = list(set([word for sentence in processed_sentences for word in sentence]))
# Create vectors for each sentence
vectors = np.array([sentence_to_vector(sentence, all_words) for sentence in processed_sentences])
# Step 4: Calculate Cosine Similarity Matrix
similarity_matrix = cosine_similarity(vectors)
# Step 5: Apply TextRank using NetworkX
nx_graph = nx.from_numpy_array(similarity_matrix)
scores = nx.pagerank(nx_graph)
# Step 6: Generate Top 50% and 25% Summaries
sentence_count = len(sentences)
top_50_percent = int(sentence_count * 0.5)
top_25_percent = int(sentence_count * 0.25)
# Sort sentences by their TextRank scores
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
# Create summaries
summary_50 = ' '.join([s for _, s in ranked_sentences[:top_50_percent]])
summary_25 = ' '.join([s for _, s in ranked_sentences[:top_25_percent]])
# Display Summaries
print('--- 50% Summary ---')
print(summary_50)
print('\n--- 25% Summary ---')
print(summary_25)
