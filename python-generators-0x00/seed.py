import mysql.connector
import csv
import uuid

# Connect to MySQL server without specifying database
def connect_db():
    """
    Connect to the ALX_prodev database using myuser.
    Returns a connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="myuser",
        password="6679",
    )


# Create the database ALX_prodev if it does not exist
def create_database(connection):
    """
    Create the database ALX_prodev if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

# Connect to the ALX_prodev database
def connect_to_prodev():
    """
    Connect to the ALX_prodev database.
    Returns a connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="ALX_prodev"
    )

# Create the user_data table if it does not exist
def create_table(connection):
    """
    Create the user_data table with columns:
    - user_id: UUID as VARCHAR(36), primary key
    - name: non-null VARCHAR(255)
    - email: non-null VARCHAR(255)
    - age: non-null DECIMAL
    """
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    )
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

# Insert data from CSV file into the user_data table,
# generate UUID for user_id automatically (CSV does NOT have user_id column)
def insert_data(connection, csv_file):
    """
    Read data from a CSV file without user_id column,
    generate a UUID for each inserted row as user_id.
    """
    cursor = connection.cursor()
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)  # expects columns: name,email,age only
        for row in reader:
            user_id = str(uuid.uuid4())  # Generate new UUID for each row
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (
                user_id,
                row['name'],
                row['email'],
                row['age']
            ))
    connection.commit()
    cursor.close()
