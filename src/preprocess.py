import os
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def extract_features(rtl_file):
    with open(rtl_file, 'r') as f:
        rtl_code = f.read()

    features = {
        'AND': rtl_code.count('AND'),
        'OR': rtl_code.count('OR'),
        'NOT': rtl_code.count('NOT'),
        'XOR': rtl_code.count('XOR'),
        # ... add more features (fan-in, fan-out, etc.) 
    }
    return features

def prepare_data(data_dir):
    X, y = [], [] 
    for file_name in os.listdir(data_dir):
        if file_name.endswith((".vhd", ".sv")): # Adjust file extensions 
            file_path = os.path.join(data_dir, file_name)
            features = extract_features(file_path)
            X.append(features)
            # You'll need logic to get the actual logic depth for 'y' 
            # (e.g., by simulating the design or using existing labels)
            y.append(random.randint(1, 10))  # Placeholder 

    # Convert to NumPy arrays
    X = np.array(X)
    y = np.array(y)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Feature scaling 
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test 

if __name__ == "__main__":
    data_dir = "data"
    X_train, X_test, y_train, y_test = prepare_data(data_dir)
    # Save the prepared data to files if needed
