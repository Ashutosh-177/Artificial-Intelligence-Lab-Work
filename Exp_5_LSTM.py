# 1. Load the basic libraries and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
warnings.filterwarnings('ignore')
# 2. Load the dataset
dataset = pd.read_csv("/content/yahoofinance.csv")
print(dataset.head())
Volume
# 3. Analyse the dataset
# Summary statistics
print(dataset.describe())
# Dataset info
print(dataset.info())
Volume
# Column Non-Null Count Dtype
None
# 4. Apply LSTM Model
# Extract the feature column for modeling
apple_training = dataset.iloc[:, 1:2].values
# Normalize the feature using Min-Max Scaler
scaler = MinMaxScaler(feature_range=(0, 1))
apple_training_scaled = scaler.fit_transform(apple_training)
# Create the feature set and labels
feature_set = []
labels = []
for i in range(60, 253):
    pass
feature_set.append(apple_training_scaled[i-60:i, 0])
labels.append(apple_training_scaled[i, 0])
# Convert to numpy arrays
feature_set = np.array(feature_set)
labels = np.array(labels)
# Reshape feature set for LSTM input
# Initialize the model
model = Sequential()
# Add LSTM layers with Dropout
model.add(Dropout(0.20))
model.add(LSTM(units=60, return_sequences=True))
model.add(Dropout(0.20))
model.add(LSTM(units=60, return_sequences=True))
model.add(Dropout(0.20))
model.add(LSTM(units=60))
model.add(Dropout(0.20))
# Add output layer
model.add(Dense(units=1))
# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
# 5. Apply the training over the dataset to minimize the loss
# 6. Observe the cost function vs iterations learning curve
# Plot cost function (loss) vs iterations (epochs)
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.title('Cost Function vs Iterations')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
plt.show()
Result
# a. Model Summary
model.summary()
# b. Training and Validation accuracy v/s epochs
# Plot training and validation accuracy
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy vs. Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
# c. Training and Validation loss v/s epochs
# Plot training and validation loss
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss vs. Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
# d. Visualize the Predicted and originalStock Price
# Prepare testing data
testing_data = dataset.iloc[:, 1:2].values
test_feature = testing_data.reshape(-1, 1)
test_feature = scaler.transform(test_feature)
testing_features = []
for i in range(60, 253):
    pass
testing_features.append(test_feature[i-60:i, 0])
testing_features = np.array(testing_features)
# Predict the stock prices
predictions = model.predict(testing_features)
predictions = scaler.inverse_transform(predictions)
# Visualize the results
plt.figure(figsize=(12, 6))
plt.plot(testing_data, color='blue', label='Real Apple Stock Price')
plt.plot(predictions, color='red', label='Predicted Apple Stock Price')
plt.title('Real vs. Predicted Apple Stock Price')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
