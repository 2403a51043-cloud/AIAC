import pandas as pd  # Data manipulation and analysis
import numpy as np   # Numerical operations (used here for log transform)

# Define input and output CSV paths
input_file = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB17\financial_data.csv"
output_file = r"LAB17/finance_updated.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(input_file)

# 1) Handle missing values in closing_price and volume
#    Strategy: forward fill -> backfill; for volume, any remaining NaNs -> 0
df['closing_price'] = pd.to_numeric(df['closing_price'], errors='coerce')
df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

df['closing_price'] = df['closing_price'].fillna(method='ffill').fillna(method='bfill')
df['volume'] = df['volume'].fillna(method='ffill').fillna(method='bfill').fillna(0)

# 2) Create lag-based return features
#    1-day return: (today - yesterday) / yesterday
df['return_1d'] = df['closing_price'].pct_change(periods=1)
#    7-day return: (today - 7 days ago) / 7 days ago
df['return_7d'] = df['closing_price'].pct_change(periods=7)

# 3) Normalize volume using log-scaling (log1p avoids log(0))
df['volume_log'] = np.log1p(df['volume'])

# 4) Detect outliers in closing_price using the IQR rule
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Mark outliers in a boolean column
df['closing_price_outlier'] = ((df['closing_price'] < lower_bound) | (df['closing_price'] > upper_bound))

# Save the updated DataFrame to CSV in LAB17 folder
df.to_csv(output_file, index=False)
