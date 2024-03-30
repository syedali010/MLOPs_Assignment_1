import os
import pytest
import pandas as pd
import joblib
import numpy as np

# Determine the directory of this file to construct the path to the CSV file
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(THIS_DIR, 'Customer_segmentation.csv')
MODEL_FILE = os.path.join(THIS_DIR, 'customer_segmentation_model.pkl')


@pytest.fixture
def trained_model():
    """
    Fixture to load the trained model from a file.
    Checks if the model file exists before loading to prevent FileNotFoundError.
    """
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(f"{MODEL_FILE} does not exist.")
    model = joblib.load(MODEL_FILE)
    return model


@pytest.fixture
def test_data():
    """
    Fixture to load test data, converting gender to numeric.
    Ensures the CSV file is correctly located and raises a clear error if not found.
    """
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(f"{CSV_FILE} does not exist.")
    data = pd.read_csv(CSV_FILE)
    data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
    columns = ['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    X_test = data[columns]
    return X_test


def test_prediction(trained_model, test_data):
    """
    Test predictions are of correct shape and within expected range.
    Validates model predictions against test data, ensuring correct output shape and value range.
    """
    model = trained_model
    X_test = test_data
    predictions = model.predict(X_test)
    
    assert predictions.shape[0] == X_test.shape[0], "Prediction shape mismatch."
    assert np.all(predictions >= 0) and np.all(predictions < 5), "Prediction values out of expected range."
