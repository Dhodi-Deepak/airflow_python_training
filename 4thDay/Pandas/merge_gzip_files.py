import dask.dataframe as dd

# Define the data types for your columns to prevent the error
dtypes = {
    'Customer_Id': 'object'
}

# Read all matching CSV files, now with the correct data types
# Adding `compression='gzip'` is also a good practice for robustness
ddf = dd.read_csv(
    'not_renewed_shards_20250812*.csv.gzip',
    dtype=dtypes,
    compression='gzip'
)

# This will now write the output without the ValueError
ddf.to_csv('not_renewed_shards.csv.gzip')

print("Files have been merged successfully.")