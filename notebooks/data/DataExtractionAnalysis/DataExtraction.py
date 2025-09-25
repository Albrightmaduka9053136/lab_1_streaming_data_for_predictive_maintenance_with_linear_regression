# DataExtraction.py
"""
Module for extracting data for linear regression predictive maintenance workshop.
"""
import pandas as pd
import os

def load_data(file_path):
    """
    Loads data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

# Example usage
if __name__ == "__main__":
    data_path = "../data/original_training_data.csv"
    try:
        df = load_data(data_path)
        print(f"Loaded data with shape: {df.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
