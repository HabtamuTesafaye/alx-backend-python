# 🧠 Python Generators doc

> **Part of the ALX Backend Specialization**
> This project showcases the use of **Python generators** to handle large-scale data from a SQL database efficiently.

---

## 📁 Project Overview

This repository demonstrates how **generators** (`yield`) in Python can be used to:

* Stream data **row-by-row** from a MySQL database
* Process data in **batches**
* Implement **lazy pagination**
* Compute **aggregates** (like average) without loading the full dataset

The data source is a seeded MySQL table populated from a `user_data.csv` file.

---

## 📂 Directory Contents

| File                    | Description                                                                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `seed.py`               | 📦 Initializes and seeds the MySQL database (`ALX_prodev`) and table (`user_data`). Includes helper functions to create DB, create table, and insert CSV data.                                                |
| `user_data.csv`         | 📄 Sample user dataset. Contains UUIDs, names, emails, and ages for seeding the DB.                                                                                                                           |
| `0-stream_users.py`     | 🔁 Defines `stream_users()`, a generator function that yields each user row one by one. Useful for streaming large datasets efficiently.                                                                      |
| `1-batch_processing.py` | 📦 Contains two functions:<br>• `stream_users_in_batches(batch_size)` – yields data in batches of size `batch_size`.<br>• `batch_processing(batch_size)` – filters and prints users over age 25.              |
| `2-lazy_paginate.py`    | 📄 Implements paginated access using generators:<br>• `paginate_users(page_size, offset)` – fetches data with `LIMIT/OFFSET`.<br>• `lazy_pagination(page_size)` – lazily yields each page of users as needed. |
| `4-stream_ages.py`      | 📊 Memory-efficient average calculation:<br>• `stream_user_ages()` – yields user ages.<br>• `calculate_average_age()` – computes average without using SQL `AVG()`.                                           |
| `README.md`             | 📘 This file. Repository and file structure documentation.                                                                                                                                                    |

---
## 🏃‍♂️ Options to Run Script

| Script      | Purpose                                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| `0-main.py` | 🧪 Run the full database setup: create DB, create table, insert CSV data, and confirm setup.         |
| `1-main.py` | 🧪 Test streaming users one-by-one; prints the first 6 users from the database.                      |
| `2-main.py` | 🧪 Test batch processing: filters and prints users older than 25 in batches.                         |
| `3-main.py` | 🧪 Test paginated lazy loading of users using the generator-based pagination.                        |
| `4-main.py` | 🧪 Test average age calculation by streaming user ages and computing average in Python (no SQL AVG). |

---


## 🧪 What Each File Demonstrates

### `seed.py` – Database Bootstrapping

* Connects to MySQL
* Creates `ALX_prodev` database and `user_data` table (if not exists)
* Reads `user_data.csv` and inserts rows with `INSERT IGNORE`
* Helper functions:

  * `connect_db()`
  * `create_database()`
  * `connect_to_prodev()`
  * `create_table()`
  * `insert_data()`

---

### `0-stream_users.py` – Row-by-Row Streaming

```python
def stream_users():
    # Connects to the DB and yields each user row one by one.
```

💡 Uses a single `for` loop to yield dictionary rows lazily from the DB. Helps avoid loading all rows into memory.

---

### `1-batch_processing.py` – Batch Loading and Filtering

```python
def stream_users_in_batches(batch_size):
    # Yields user rows in chunks of batch_size.

def batch_processing(batch_size):
    # Uses the batch stream to filter and print users over age 25.
```

💡 Demonstrates batch loading (a common real-world optimization) and simple data filtering.

---

### `2-lazy_paginate.py` – Lazy Pagination with Generators

```python
def paginate_users(page_size, offset):
    # Fetches users using LIMIT and OFFSET.

def lazy_pagination(page_size):
    # Generator that lazily fetches paginated user data.
```

💡 Emulates APIs with paginated endpoints, loading pages only as needed. Efficient for infinite scroll or UI paginators.

---

### `4-stream_ages.py` – Memory-Efficient Aggregation

```python
def stream_user_ages():
    # Yields ages one at a time.

def calculate_average_age():
    # Calculates average age using generator without loading all ages at once.
```

💡 Replaces SQL `AVG()` with Python logic, emphasizing generator-based computation for large datasets.

---

## 🧪 Basic Usage Example

Here’s a minimal example showing how you might use the `seed.py` module to set up your database and insert data:

```python
import seed

def main():
    # Connect to MySQL server (without selecting DB)
    connection = seed.connect_db()
    if connection:
        seed.create_database(connection)
        connection.close()
        print("Database created or already exists.")

    # Connect to the created database
    connection = seed.connect_to_prodev()
    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')
        print("Table created and data inserted successfully.")
        connection.close()

if __name__ == "__main__":
    main()
```

Run this script with:

```bash
python3 main.py
```

---

## 📎 Dependencies & Setup

### Python version

* Python 3.x (tested with 3.8+)

### Install MySQL Connector

```bash
pip install mysql-connector-python
```

### MySQL Server

Make sure MySQL server is running and you have a user with privileges to:

* create databases
* create tables
* insert data

Example user in `seed.py` is `myuser` with password `6679`.

---

## 🙋‍♀️ Author

**Habtamu Tesfaye**

---

