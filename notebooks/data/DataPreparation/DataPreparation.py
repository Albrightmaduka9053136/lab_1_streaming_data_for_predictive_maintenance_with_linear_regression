# DataPreparation.py
"""
Module for preparing data for linear regression predictive maintenance workshop.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, feature_cols, target_col):
    """
    Preprocesses the data by splitting into train/test and scaling features.
    Args:
        df (pd.DataFrame): Input data.
        feature_cols (list): List of feature column names.
        target_col (str): Target column name.
    Returns:
        X_train, X_test, y_train, y_test, scaler
    """
    X = df[feature_cols]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler

# Example usage
if __name__ == "__main__":
    # Example: Load data and preprocess
    # in data/DataPreparation/DataPreparation.py
    from data.DataExtractionAnalysis import load_data
    data_path = "../data/original_training_data.csv"
    df = load_data(data_path)
    feature_cols = [col for col in df.columns if col != 'target']
    target_col = 'target'
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df, feature_cols, target_col)
    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
