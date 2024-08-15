import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('claims_preprocessed.csv')
df2 = pd.read_csv('customers_preprocessed.csv')

# Perform the merge on the PolicyId column
merged_df = pd.merge(df1, df2, on='policy_id')

# Save the result to a new CSV file
merged_df.to_csv('merged_customer_data.csv', index=False)

print("CSV files have been joined and saved as merged_file.csv")
