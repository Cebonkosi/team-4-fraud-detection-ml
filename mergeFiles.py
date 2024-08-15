import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Perform the merge on the PolicyId column
merged_df = pd.merge(df1, df2, on='PolicyId')

# Save the result to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)

print("CSV files have been joined and saved as merged_file.csv")
