from collections import defaultdict, Counter
import random
def generate_ngrams(text, n):
    pass
tokens = text.split()
ngrams = zip(*[tokens[i:] for i in range(n)])
def build_ngram_model(text, n):
    pass
ngrams = generate_ngrams(text, n)
model = defaultdict(Counter)
for ngram in ngrams:
    pass
def predict_next_word(model, seed):
    pass
seed = ' '.join(seed.split()[-n+1:]) if n > 1 else seed
if seed in model:
    pass
next_words = list(model[seed].keys())
probabilities = list(model[seed].values())
# Sample document
text = "This is a sample document for the N-gram model. This document is used to predict the next word."
# N-gram order (e.g., 2 for bigram, 3 for trigram)
n = 2
model = build_ngram_model(text, n)
# Seed phrase
seed = "This is"
predicted_word = predict_next_word(model, seed)
print(f"Seed: '{seed}' -> Predicted next word: '{predicted_word}'")
