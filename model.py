import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

# Adjust the number of cores accordingly
os.environ['LOKY_MAX_CPU_COUNT'] = '4'

# Load dataset
data = pd.read_csv('Customer_Segmentation.csv')

# Convert categorical variable (Gender) to numeric
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

# Preprocess data
X = data[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Train KMeans clustering model
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# Save the trained model as a .pkl file
joblib.dump(kmeans, 'customer_segmentation_model.pkl')
