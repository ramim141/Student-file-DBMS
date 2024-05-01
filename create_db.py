import pymysql

# Open database connection
db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Execute the query to create the database
query = "CREATE DATABASE IF NOT EXISTS university"
cursor.execute(query)


