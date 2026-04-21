import spacy
from collections import Counter
# Load spaCy model
nlp = spacy.load("en_core_web_sm")
def extract_keywords(text, top_n=25):
    pass
doc = nlp(text)
keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]
keyword_freq = Counter(keywords)
def analyze_keywords(keywords):
    pass
for word, freq in keywords:
    pass
if freq < 2:
    pass
elif len(word) < 4:
    pass
else:
    pass
# Your portfolio text
# Extract top 25 keywords
top_keywords = extract_keywords(portfolio)
print("Top 25 Keywords:", top_keywords)
# Analyze keywords
analysis = analyze_keywords(top_keywords)
for category, words in analysis.items():
    pass
print(f"{category}: {words}")
