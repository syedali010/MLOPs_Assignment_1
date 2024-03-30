import pytest
import pandas as pd
import joblib
import numpy as np

@pytest.fixture
def trained_model():
    # Load the trained model from the file
    model = joblib.load('customer_segmentation_model.pkl')
    return model

@pytest.fixture
def test_data():
    # Load test data
    data = pd.read_csv('Customer_segmentation.csv')
    # Convert gender to numeric
    data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
    X_test = data[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    return X_test

def test_prediction(trained_model, test_data):
    model = trained_model
    X_test = test_data
    # Make predictions
    predictions = model.predict(X_test)
    # Check if predictions are of correct shape
    assert predictions.shape[0] == X_test.shape[0]
    # Check if predictions are within expected range (cluster labels)
    assert np.all(predictions >= 0) and np.all(predictions < 5)
