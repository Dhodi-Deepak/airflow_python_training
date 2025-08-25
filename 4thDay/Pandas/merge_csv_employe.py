import pandas as pd

df = pd.read_csv('employee1.csv')
df2 = pd.read_csv('employee2.csv')
print(df)
print(df2)

merged_df = pd.concat([df, df2], ignore_index=True)
print(merged_df)
merged_df.to_csv('merged_employee.csv')
