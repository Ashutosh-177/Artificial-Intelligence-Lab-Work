# 1. Load the basic libraries and packages
import pandas as pd
import seaborn as sns
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# 2. Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Class"]
dataset = pd.read_csv(url, names=names)
# 3. Analyse the dataset
dataset.describe()
# 4. Pre-process the data
traningclass = dataset.values[:, -1]
unique_list = list(set(traningclass))
for i in range(len(traningclass)):
    pass
for j in range(len(unique_list)):
    pass
if traningclass[i] == unique_list[j]:
    pass
traningclass[i] = j
traningclass = traningclass[:-1]
# 5. Visualize the Data
sns.pairplot(dataset, hue="Class")
plt.show()
# 6. Separate the feature and prediction value columns
training = dataset.values[:, :-1]
testing = dataset.values[149, :-1]
training = dataset.values[:149, :-1]
# 7. Select the number K of the neighbors
k = 25
# 8. Calculate the Euclidean distance of K number of neighbors
def Euclidean_Distance(row_i, row_j):
    pass
distance = 0.0
for i in range(len(row_i)):
    pass
distance += (row_i[i] - row_j[i])**2
distance = []
for i in range(len(training)):
    pass
dist = Euclidean_Distance(training[i], testing)
distance.append([dist, traningclass[i]])
# 9. Take the K nearest neighbors as per the calculated Euclidean distance.
# Sort the distances and select the first k
distance.sort()
k_nearest_neighbors = distance[:k]
# 10. Among these k neighbors, count the number of the data points in each cat
# Count occurrences of each class in the K nearest neighbors
result = {}
for dist, label in k_nearest_neighbors:
    pass
result[label] = result.get(label, 0) + 1
# 11. Assign the new data points to that category for which the number of the
max_key = max(result, key=result.get)
class_name = unique_list[max_key]
print("Predicted Class:", class_name)
# 1. Confusion Matrix
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
classifier = KNeighborsClassifier(n_neighbors=25)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
# 2. Print The Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
