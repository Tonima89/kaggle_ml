import kagglehub
import pandas as pd
import os

print("Sir-er dataset download shuru hocche...")

# 1. Dataset path
path = kagglehub.dataset_download("abhishek14398/salary-dataset-simple-linear-regression")
print("Dataset successfully downloaded to:", path)

# 2. Files list tracking
files = os.listdir(path)

# 3. CSV dynamic read
csv_file = [f for f in files if f.endswith('.csv')][0] if any(f.endswith('.csv') for f in files) else files[0]
csv_file_path = os.path.join(path, csv_file)

# 4. Read using pandas
df = pd.read_csv(csv_file_path)

print("\nDataset er prothom 5 ti row:")
print(df.head())
print("\nDataset-er total (Row, Column) সংখ্যা:")
print(df.shape)