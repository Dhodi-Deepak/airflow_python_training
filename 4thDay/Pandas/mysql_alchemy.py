import pandas as pd
from sqlalchemy import create_engine

db_connection_str = (
    "mysql+mysqlconnector://evergent:gr3%40t@"
    "nonprod.cluster-cv87vflxcrgb.eu-west-1.rds.amazonaws.com:3306/ccbuser"
)
db_engine = create_engine(db_connection_str)
sql_query = "SELECT * FROM bill_status;"
try:
    df = pd.read_sql_query(sql_query, db_engine)
    print("Data fetched successfully:")
    print(df)
except Exception as e:
    print(f"An error occurred: {e}")
finally:

    if 'db_engine' in locals():
        db_engine.dispose()
