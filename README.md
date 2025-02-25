# RTL Logic Depth Prediction

This project aims to develop an AI algorithm to predict the combinational logic depth of signals in RTL designs for early identification of potential timing violations.

## Project Structure

- **data/:** Contains RTL design dataset (or scripts to generate it).
  - `generate_data.py`: Script to generate placeholder RTL design data.
- **src/:** Source code for data preprocessing, model training, and evaluation.
  - `preprocess.py`: Preprocesses the RTL design data and extracts features.
  - `model.py`: Builds, trains, and saves the neural network model.
  - `evaluate.py`: Loads the trained model and evaluates its performance.
- **models/:** Stores trained machine learning models.
- **requirements.txt:** Lists the dependencies required for the project.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

#. **Clone the repository:**
   '''
  > git clone https://github.com/gunjan975/-AI-based-Timing-Violation-Predictor.git
  > cd -AI-based-Timing-Violation-Predictor
   '''
#. Install dependencies:
   > pip install -r requirements.txt

#.Data Generation
   > python data/generate_data.py

#.Data Preprocessing
   > python src/preprocess.py

#.Model Training
   > python src/model.py

#.Model Evaluation
   > python src/evaluate.py

#These dependencies are listed in the requirements.txt file.
  > pip install -r requirements.txt 
