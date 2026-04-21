import pandas as pd
cosine
recommend_to = 3
sim_score=list(enumerate(cosine[recommend_to]))
sim_score
sorted_scores=sorted(sim_score,key=lambda x:x[1],reverse = True)
sorted_scores
top_n = 2
extract_items = sorted_scores[1:top_n+1]
extract_items
