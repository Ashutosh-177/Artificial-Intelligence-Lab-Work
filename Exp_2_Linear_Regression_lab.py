# 1. Load the basic libraries and packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# 2. Load the dataset
dataset = pd.read_csv("/content/Dataset.csv")
dataset.head()
# 3. Analyse the dataset
dataset.describe()
# 4. Pre-process the data
dataset = dataset.dropna()
# 5. Visualize the Data
plt.scatter(dataset['x'],dataset['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
# 6. Separate the feature and prediction value columns
x_feature = np.array(dataset['x'])
y_feature = np.array(dataset['y'])
# 7.Write the Hypothesis Function
def Hypothesis(theta_array , x) :
    pass
# 8. Write the Cost Function
def Cost_Function(theta_array,x,y , m):
    pass
total_cost = 0
for i in range(m):
    pass
total_cost += (Hypothesis(theta_array,x[i]) - y[i])**2
# 9. Write the Gradient Descent optimization algorithm
def Gradient_Descent(theta_array , x, y , m ,alpha) :
    pass
summation_0 = 0
summation_1 = 0
for i in range(m):
    pass
summation_0 += (Hypothesis(theta_array,x[i]) - y[i])
summation_1 += ((Hypothesis(theta_array,x[i]) - y[i])*x[i])
new_theta0 = theta_array[0] - (alpha/m)*summation_0
new_theta1 = theta_array[1] - (alpha/m)*summation_1
new_theta = [new_theta0 , new_theta1]
# 10. Apply the training over the dataset to minimize the loss
cost_values = []
def Training(x, y, alpha, epochs):
    pass
theta_0 = 0
theta_1 = 0
theta_array = [theta_0, theta_1]
m = len(x)
for i in range(epochs):
    pass
theta_array = Gradient_Descent(theta_array, x, y, m, alpha)
loss = Cost_Function(theta_array, x, y, m)
cost_values.append(loss)
y_new = theta_array[0] + theta_array[1]*x
if i == epochs-1 :
    pass
plt.plot(x, y_new , 'r')
plt.scatter(x, y)
plt.show()
# 11. Find the best fit line to the given dataset
alpha = 0.0001
epochs = 100
Training(x_feature , y_feature , alpha , epochs)
# 12. Observe the cost function vs iterations learning curve
x = np.arange(0, epochs)
plt.plot(x, cost_values)
plt.xlabel('Epochs')
plt.ylabel('Cost')
plt.show()
