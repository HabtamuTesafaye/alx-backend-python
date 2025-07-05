import seed

def stream_users():
    """
    Generator function that connects to the 'ALX_prodev' database,
    queries all rows from the 'user_data' table, and yields one row at a time.

    Important:
    - This function returns a generator object.
    - It does NOT print anything by itself.
    - To see output, you must iterate over the generator.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # Fetch rows as dicts
    cursor.execute("SELECT * FROM user_data")
    
    for row in cursor:
        print(row)      # prints immediately
        yield row       # still yields the row
    
    cursor.close()
    connection.close()

