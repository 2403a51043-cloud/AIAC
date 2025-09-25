import pandas as pd  # Data manipulation and analysis

# Define input and output file paths for IoT sensor data
input_file = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB17\iot_sensor.csv"
output_file = r"C:\Users\manic\OneDrive\Desktop\AIAC\LAB17\iot_updated.csv"

# Load the IoT sensor dataset into a DataFrame
df = pd.read_csv(input_file)

# 1) Handle missing values using forward fill (propagate last valid value)
df = df.fillna(method='ffill')

# 2) Remove sensor drift using rolling mean (window=5, centered) for smoothing
if 'temperature' in df.columns:
    df['temperature'] = df['temperature'].rolling(window=5, min_periods=1, center=True).mean()
if 'humidity' in df.columns:
    df['humidity'] = df['humidity'].rolling(window=5, min_periods=1, center=True).mean()

# 3) Normalize readings using standard scaling (z-score: (x - mean) / std)
for col in ['temperature', 'humidity']:
    if col in df.columns:
        mean = df[col].mean()
        std = df[col].std()
        if std != 0:
            df[col + '_scaled'] = (df[col] - mean) / std
        else:
            df[col + '_scaled'] = 0

# 4) Encode categorical sensor IDs to numeric codes
if 'sensor_id' in df.columns:
    df['sensor_id_encoded'] = df['sensor_id'].astype('category').cat.codes

# Save the updated DataFrame to CSV in LAB17 folder
df.to_csv(output_file, index=False)
print(f"Wrote CSV to: {output_file}")

