import os
import pytest
import pandas as pd
import joblib
import numpy as np

# Get the directory of this file to construct absolute path
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(THIS_DIR, 'Customer_segmentation.csv')


@pytest.fixture
def trained_model():
    """Fixture to load the trained model from a file."""
    model = joblib.load('customer_segmentation_model.pkl')
    return model


@pytest.fixture
def test_data():
    """Fixture to load test data, converting gender to numeric."""
    data = pd.read_csv(DATA_FILE)
    data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
    columns = ['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    X_test = data[columns]
    return X_test


def test_prediction(trained_model, test_data):
    """Test predictions are of correct shape and within expected range."""
    model = trained_model
    X_test = test_data
    predictions = model.predict(X_test)
    
    assert predictions.shape[0] == X_test.shape[0]
    assert np.all(predictions >= 0) and np.all(predictions < 5)
