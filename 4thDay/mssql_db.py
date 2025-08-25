import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=34.252.3.109;"
    "DATABASE=YourDatabaseName;"
    "UID=dazb_b2b;"
    "PWD=Y340ufgrP@sgswhhnmE3d;"
)

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SQL query
    cursor.execute("SELECT FirstName, LastName FROM dbo.Employees")

    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(f"{row.FirstName} {row.LastName}")

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    print(f"Error connecting to database: {sqlstate}")

finally:
    # Ensure the connection is always closed
    if 'conn' in locals() and conn:
        conn.close()
        print("Connection closed.")