import numpy as np
import pandas as pd
from surprise import SVD,KNNBasic,Dataset,Reader
from surprise.model_selection import cross_validate
#providing the rating matrix
users = [1,2,3,4,1,2,3,4]
movies = ["starwars","harrypoter","starwars","starwars","harrypoter","tomraider","harrypoter","tomraider"]
rating = [1,3,4,2,3,4,1,1]
df = pd.DataFrame(rating_dict)
df
algo = SVD()
reader = Reader(rating_scale=(1,5))
data=Dataset.load_from_df(df[["userID","ItemID","rating"]],reader)
cross_validate(algo,data,measures=["RMSE","MAE"],cv=5,verbose=True)
algo.predict(3,"starwars")
Prediction(uid=3, iid='starwars', r_ui=None, est=2.5155979062028475, details={'was_impossible': False})
algo.predict(1,"tomraider")
Prediction(uid=1, iid='tomraider', r_ui=None, est=2.0879340790229786, details={'was_impossible': False})
