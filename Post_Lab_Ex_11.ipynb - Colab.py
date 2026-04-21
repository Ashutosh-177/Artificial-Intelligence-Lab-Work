import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#Load the IMDB data
df = pd.read_csv('/content/imdb_top_1000.csv')
# Filter only TV Series
series_df = df[df['Series_Title'].str.contains('(?i)series|season|tv', na=False)].copy()
# If 'Overview' column exists, we use it; else, use 'Description' or similar
text_col = 'Overview' if 'Overview' in series_df.columns else 'Description'
# Drop rows with missing overview/description
series_df = series_df.dropna(subset=[text_col])
# Reset index after filtering
series_df.reset_index(drop=True, inplace=True)
# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(series_df[text_col])
# Cosine Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# Pick one series to recommend from (e.g., first one)
recommend_to = 0
# Get similarity scores for this series
sim_scores = list(enumerate(cosine_sim[recommend_to]))
# Sort by similarity score
sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
# Get top 10 similar series (excluding the selected one)
top_n = 10
recommended = sorted_scores[1:top_n+1]
# Show the recommended series
