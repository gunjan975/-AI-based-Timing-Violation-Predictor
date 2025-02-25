import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_squared_error, r2_score 
from preprocess import prepare_data

# Load the saved model
model = keras.models.load_model("models/logic_depth_model.h5")

# Load and preprocess the test data
data_dir = "data" 
X_train, X_test, y_train, y_test = prepare_data(data_dir)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}") 
