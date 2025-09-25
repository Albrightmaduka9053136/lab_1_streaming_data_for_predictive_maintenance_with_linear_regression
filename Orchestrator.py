# Orchestrator.py
"""
Main orchestrator for linear regression predictive maintenance workflow.
"""
from data.DataExtractionAnalysis import load_data
from data.DataPreparation import preprocess_data


def main():
    data_path = "data/original_training_data.csv"
    df = load_data(data_path)
    feature_cols = [col for col in df.columns if col != 'target']
    target_col = 'target'
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df, feature_cols, target_col)
    print("Data preparation complete.")
    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    # Add model training, evaluation, and other workflow steps here

if __name__ == "__main__":
    main()
