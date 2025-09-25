# Lab 1: Streaming Data for Predictive Maintenance with Linear Regression–Based Alerts
# Repository: lab_1_streaming_data_for_predictive_maintenance_with_linear_regression
# Title: Predictive Maintenance Pipeline
# Author: Albright Maduka
# Course: CSCN 8010

# Aim
Detect early signs of abnormal behavior in a robot before breakdown by modeling time (X‑axis) against current readings (Y‑axis) and flagging anomalies with thresholded residuals.

# Requirements & Setup
All required packages are listed in requirements.txt.
Install with:

python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt


# Key packages:
pandas
numpy
matplotlib
scikit-learn
SQLAlchemy
psycopg2-binary
Artifacts & Outputs

# Artifacts & Outputs
* All output CSVs are in artifacts/
alerts_log.csv
model_params.csv
summary_dashboard.csv
test_residuals.csv
test_with_predictions.csv
thresholds.csv
train_residuals.csv
* All plots are in artifacts/plots/

![Axis 1 Test Observed vs Regression](artifacts/plots/axis1_test_observed_vs_regression.png)

![Axis 1 Test Residuals](artifacts/plots/axis1_test_residuals.png)

![Axis 2 Test Observed vs Regression](artifacts/plots/axis2_test_observed_vs_regression.png)

![Axis 2 Test Residuals](artifacts/plots/axis2_test_residuals.png)

![Axis 3 Test Observed vs Regression](artifacts/plots/axis3_test_observed_vs_regression.png)

![Axis 3 Test Residuals](artifacts/plots/axis3_test_residuals.png)

![Axis 4 Test Observed vs Regression](artifacts/plots/axis4_test_observed_vs_regression.png)

![Axis 4 Test Residuals](artifacts/plots/axis4_test_residuals.png)

![Axis 5 Test Observed vs Regression](artifacts/plots/axis5_test_observed_vs_regression.png)

![Axis 5 Test Residuals](artifacts/plots/axis5_test_residuals.png)

![Axis 6 Test Observed vs Regression](artifacts/plots/axis6_test_observed_vs_regression.png)

![Axis 7 Test Residuals](artifacts/plots/axis7_test_residuals.png)

![Axis 7 Test Observed vs Regression](artifacts/plots/axis7_test_observed_vs_regression.png)

![Axis 8 Test Residuals](artifacts/plots/axis8_test_residuals.png)

![Axis 8 Test Observed vs Regression](artifacts/plots/axis8_test_observed_vs_regression.png)

![Univariate Axis 1](artifacts/plots/univariate_axis1.png)

![Univariate Axis 2](artifacts/plots/univariate_axis2.png)

![Univariate Axis 3](artifacts/plots/univariate_axis3.png)

![Univariate Axis 4](artifacts/plots/univariate_axis4.png)

![Univariate Axis 5](artifacts/plots/univariate_axis5.png)

![Univariate Axis 6](artifacts/plots/univariate_axis6.png)

![Univariate Axis 7](artifacts/plots/univariate_axis7.png)

![Univariate Axis 8](artifacts/plots/univariate_axis8.png)




# Workflow
1. Database Integration:
 - Connect to NeonDB, download and preprocess measurements, save as CSV.

2. Streaming Simulation:
 - Generate synthetic data matching training statistics.

3. Regression Models & Residual Analysis:
- Train linear regression models, compute and save residuals.

4. Thresholds & Anomaly Detection:
- Calculate alert/error thresholds, detect events, save results.

5. Visualization:
- Generate and save per-axis plots with event markers.

6. Summary Dashboard:
- Summarize alerts and errors in dashboard CSV.

# Data Dictionary
* time — original timestamp (ISO‑8601, UTC)
* __time_s — elapsed seconds from first training timestamp
* axis1 … axis8 — current readings per axis
* {axis}_resid — residuals = observed − predicted
* thresholds.csv — columns: axis, sigma, MinC, MaxC, T_seconds
* alerts_log.csv — columns: axis, level, start_time, end_time, duration_sec, peak_residual
* summary_dashboard.csv — columns: axis, alerts, errors, longest_event_s

# Quickstart
* Install requirements (see above).
* Run your notebook or script to:
- Export training CSV from NeonDB
- Generate synthetic CSV
- Train regression models
- Compute residuals, thresholds, and events
- Render plots and dashboards
* Review CSV outputs in artifacts/ and plots in artifacts/plots/.