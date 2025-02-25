import tensorflow as tf
from tensorflow import keras
from preprocess import prepare_data

# Load the prepared data
data_dir = "data"
X_train, X_test, y_train, y_test = prepare_data(data_dir)

# Build a simple neural network model 
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1) # Output layer for regression
])

# Compile the model
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, 
                    validation_data=(X_test, y_test), verbose=2) 

# Save the trained model
model.save("models/logic_depth_model.h5")
