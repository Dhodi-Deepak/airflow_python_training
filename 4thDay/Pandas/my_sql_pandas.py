import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


try:
    connection = mysql.connector.connect(
    host="nonprod.cluster-cv87vflxcrgb.eu-west-1.rds.amazonaws.com",
    user="evergent",
    password="gr3@t",
    port="3306",
    database="ccbuser"
)

    if connection.is_connected():
        print("Successfully connected to the database!")
        cursor = connection.cursor()
        print("\n=== READ Records ===")
        df = pd.read_sql_query("SELECT * FROM bill_status", connection)
        print(df)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection to free up resources
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")