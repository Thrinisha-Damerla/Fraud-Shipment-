import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(filepath):
    # Load dataset from CSV
    dataset = pd.read_csv(filepath)
    
    # Convert datetime columns to datetime dtype
    dataset['Creation Datetime'] = pd.to_datetime(dataset['Creation Datetime'])
    dataset['Delivery Success Datetime'] = pd.to_datetime(dataset['Delivery Success Datetime'])
    
    # Create delivery time feature in minutes
    dataset['delivery_time_mins'] = (
        dataset['Delivery Success Datetime'] - dataset['Creation Datetime']
    ).dt.total_seconds() / 60
    
    label_encoders = {}
    for col in ['pickup hub id', 'Delivery Success Hub ID', 'Shop Name', 'Rider Name']:
        le = LabelEncoder()
        dataset[col] = dataset[col].astype(str)
        dataset[col] = le.fit_transform(dataset[col])
        label_encoders[col] = le
    
    return dataset, label_encoders

# Usage example:
filepath = r"C:\Users\thrin\OneDrive\Desktop\hackathon\dataset.csv"
dataset, label_encoders = load_and_preprocess(filepath)
print(dataset.head())
