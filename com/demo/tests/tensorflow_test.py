import tensorflow as tf
from tensorflow import keras


<<<<<<< HEAD
mnist = tf.keras.datasets.mnist;
model = keras.Sequential();
# Adds a densely-connected layer with 64 units to the model:
model.add(keras.layers.Dense(64, activation='relu'));
# Add another:
model.add(keras.layers.Dense(64, activation='relu'));
# Add a softmax layer with 10 output units:
model.add(keras.layers.Dense(10, activation='softmax'));

=======
print tf.__version__
>>>>>>> origin/development
