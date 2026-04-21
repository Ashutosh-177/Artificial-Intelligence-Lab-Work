# Importing the Necessary Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# 1.Load a dataset in your IDE
dataset = pd.read_csv("/content/googleplaystore_v2.csv")
# 2.Observe the statistics of all the features
dataset.describe()
# 3.Obtain the shape of the dataset
dataset.shape
# 4.Separate all the features
dataset.info()
# Column Non-Null Count Dtype
# 5.Fill the missing values, if any, using the statistically relevant value
# Remove the Observation Having the NULL Values
dataset = dataset.drop(dataset[dataset['Rating'].isnull()].index)
# Replacing the NULL Values with DUMMY Values
# 6.Observe the Box-Plot of each feature
sns.set_style('darkgrid')
colors = ['#FFA07A', '#6495ED']
# Box plot for Rating
# Box plot for Size
plt.tight_layout()
plt.show()
