# 1. Load the basic libraries and packages
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from spacy import displacy
from PIL import Image
import io
import cairosvg
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
# Sample Text
# 1. Tokenization
sent_tokens = sent_tokenize(text)
word_tokens = word_tokenize(text)
print("\nSentence Tokenization:")
print(sent_tokens)
print("\nWord Tokenization:")
print(word_tokens)
# 2. Filtration
filtered_tokens = [word for word in word_tokens if word.isalpha()]
print("After Filtration (Only Words):")
print(filtered_tokens)
# 3. Stopwords Removal
stop_words = set(stopwords.words('english'))
print("After Stopwords Removal:")
# 4. PoS Tagging
# 5. Noun Phrase Chunking
# 6. Dependency Parsing
aux
