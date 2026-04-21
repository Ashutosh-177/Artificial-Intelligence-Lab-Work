# 1. Load the basic libraries and packages
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
# 2. Load the dataset
from tensorflow.keras.datasets import fashion_mnist
# Load Fashion MNIST dataset
# Split data into training and validation sets
# 3. Analyse the dataset
print(f"Training data shape: {train_X.shape}, Labels shape: {train_Y.shape}")
print(f"Validation data shape: {valid_X.shape}, Labels shape: {valid_Y.shape}")
print(f"Test data shape: {test_X.shape}, Labels shape: {test_Y.shape}")
print("Unique classes:", np.unique(train_Y))
# 4. Normalize the data
# Normalize pixel values to range 0-1
train_X = train_X.astype('float32') / 255.0
valid_X = valid_X.astype('float32') / 255.0
test_X = test_X.astype('float32') / 255.0
# 5. Pre-process the data
# Reshape to include channel dimension
train_X = train_X.reshape(-1, 28, 28, 1)
valid_X = valid_X.reshape(-1, 28, 28, 1)
test_X = test_X.reshape(-1, 28, 28, 1)
# Convert labels to one-hot encoding
num_classes = 10
train_label = to_categorical(train_Y, num_classes)
valid_label = to_categorical(valid_Y, num_classes)
test_Y_one_hot = to_categorical(test_Y, num_classes)
# 6. Visualize the Data
plt.figure(figsize=(10, 5))
for i in range(10):
    pass
plt.subplot(2, 5, i + 1)
plt.imshow(train_X[i].reshape(28, 28), cmap='gray')
plt.title(f"Label: {train_Y[i]}")
plt.axis('off')
plt.tight_layout()
plt.show()
# 7. Write the CNN model function
def create_cnn_model():
    pass
model = tf.keras.Sequential()
model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
model.add(tf.keras.layers.Dropout(0.4))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='linear'))
model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
# 8. Write the Cost Function
# Categorical Crossentropy as the loss function
cost_function = tf.keras.losses.CategoricalCrossentropy()
# 9. Write the Gradient Descent optimization algorithm
# Adam optimizer with default parameters
optimizer = tf.keras.optimizers.Adam()
# 10. Apply the training over the dataset to minimize the loss
fashion_model = create_cnn_model()
# Train the model
# 11. Observe the cost function vs iterations learning curve
# Accuracy Curve
# Loss Curve
# a. Training dataset
# b. Model summary
# Before Regularization
# c. Training and validation accuracy w.r.t epochs before regularization
# Train model without regularization
# d. Training and validation loss w.r.t epochs before regularization
# e. Training and validation accuracy w.r.t epochs after regularization
# Model with Dropout Regularization
# f. Training and validation loss w.r.t epochs after regularization
# g. Original v/s predicted labels for correct predicted observations
# h. Original v/s predicted labels for incorrect predicted observations
plt.imshow(test_X[incorrect].reshape(28, 28), cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
