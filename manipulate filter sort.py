import pandas as pd
from sklearn.datasets import load_diabetes

db = load_diabetes()
df_db = pd.DataFrame(db.data, columns=db.feature_names)

print("Original Data:\n", df_db.head())

sorted_df = df_db.sort_values(by='age')
print("\nSorted Data (by age):\n", sorted_df.head())

filtered_rows = df_db.query('age > 0')
print("\nFiltered Rows (age > 0):\n", filtered_rows.head())

filtered_columns = df_db[['age', 'bp']]
print("\nFiltered Columns (age, bp):\n", filtered_columns.head())

grouped_data = df_db.groupby('age')
print("\nFirst record from each age group:\n", grouped_data.first())
