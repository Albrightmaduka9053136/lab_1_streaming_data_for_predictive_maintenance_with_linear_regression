# lab_1_streaming_data_for_predictive_maintenance_with_linear_regression

Title: Predictive maintenance pipeline
 
Aim: The aim is to detect early signs of abnormal bahavior of a robot before it breaks down. By using the time on the X - axis and current readings on the Y - axis.

Requirements and Setup
Install;
- pandas
- numpy
- matplotlib
- scikit-learn
- SQLAlchemy
- psycopg2-binary

using bash 
enter

pip install -r requirements.txt


Steps

Import libraries: pandas, numpy, matplotlib, sqlalchemy, psycopg2, sklearn

1.  Database Integration 

1.1 Connection to Neon database: Connected to my NeonDB using Sqlalchemy, tested the connection and verified the table structure (staging measurements).

1.2 Inspect Table Schema (columns & types): Checking tables.

1.3 Safe Time Conversion, Downloading and Preprocessing staging measurements from NeonDB and Saving as CSV: Downloaded my staging_measurements, converted the time column to ISO 8601, seconds, axes 1-8, saved as my original_training_data.csv.

2. Streaming Simulation
2.1 Max/Min per Axis (Train vs Synthetic): Printed the maximum and minimum current per axis for both training data and synthetic test data. 
2.2 Range (Max − Min) per Axis: Calculating the range between the currents in the Original and synthetic data: calculated the range = max − min for each axis in both training and synthetic data.
2.3 Generating synthetic data that has same mean and standard deviation as the original training data: Generated the synthetic data with the same mean(mu) and standard deviation (sigma) as the original_training data. Then saved it as csv.

3. Regression Models & Residual Analysis.
3.1 Artifacts & Paths (data/, artifacts/, plots/): Creating a folder path for the Artifacts: created a folder for my artifact or output results.
3.2 Loading the Train and Test Datasets: Loaded the training data and test data to confirm the row and column.
3.3 Converting timestamps to seconds:
- Ensured that both the training data and synthetic dataset have seconds
3.4 Train linear Regression Model and saving the model parameters as csv: 
- Fitted a linear regression using elapsed time (seconds) as the X-axis and current (axis1–axis8) as the Y-axis.

- Extracted slope and intercept values for each axis and saved the results to model_params.csv in the artifacts folder.

3.4 Residuals on Original Training Data:
- Computed residuals = (Observed − Predicted) for each axis.

- Saved results in train_residuals.csv inside the artifacts folder.

 4. Testing Residuals with Thresholds (Anomaly Detection) and saving as thresholds csv: 
- Calculated Alert threshold: MinC = 2 × sigma (T = 30 seconds ).

- Calculated Error threshold: MaxC = 3 × sigma (T= 30 seconds).

- Saved results to thresholds.csv in the artifacts folder

5. Alerts & Errors implemention

5.1 Computing Residuals (errors) on Synthetic Data

5.2 Detect Alerts & Errors

6. Visualization (16-18) 
6.1  Comparing Observed vs Regression (Visualization)
6.2 Training Regression plot (Visualization): 
6.3 Testing Residuals with Thresholds and events or testing the system for anomalies(Visualization):
- Created per-axis residual plots (axis1 - axis8) using elapsed time (seconds) on the x-axis and residuals (Observed − Predicted) on the y-axis.

- Overlaid threshold lines: Green dashed = MinC (Alert threshold) and Red dash-dot = MaxC (Error threshold)

- Plotted event markers:

Orange = ALERT events (residual ≥ MinC for ≥ T seconds)

Red = ERROR events (residual ≥ MaxC for ≥ T seconds)

- Saved outputs to plots/ inside the artifacts folder (e.g., axis1_test_residuals.png).
- Note: Why there are no errors and only alerts is because the synthetic data did not produce residuals large enough and long enough to exceed the error threshold (MaxC)

6.4 Summary Dashoard of Alerts and Errors : 
- the summary of the alerts and errors that was seen


