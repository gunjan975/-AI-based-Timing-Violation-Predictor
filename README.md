This project aims to develop an AI algorithm to predict the combinational logic 
depth of signals in RTL designs for early identification of potential timing violations. 

## Project Structure

- **data/:** Contains RTL design dataset (or scripts to generate it).
- **src/:**  Source code for data preprocessing, model training, and evaluation.
- **models/:**  Stores trained machine learning models. 

## Getting Started

1. **Install dependencies:** `pip install -r requirements.txt`
2. **Generate Data (optional):** `python data/generate_data.py`
   -  **Important:** Replace the placeholder code with your own logic.
3. **Preprocess Data:** `python src/preprocess.py`
4. **Train the Model:** `python src/model.py`
5. **Evaluate the Model:** `python src/evaluate.py`
