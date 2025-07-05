# 🧠 Python Generators – `python-generators-0x00`

> **Part of the ALX Backend Specialization**  
> This project showcases the use of **Python generators** to handle large-scale data from a SQL database efficiently.

---

## 📁 Project Overview

This repository demonstrates how **generators** (`yield`) in Python can be used to:

- Stream data **row-by-row** from a MySQL database
- Process data in **batches**
- Implement **lazy pagination**
- Compute **aggregates** (like average) without loading the full dataset

The data source is a seeded MySQL table populated from a `user_data.csv` file.

---

## 📂 Directory Contents

| File | Description |
|------|-------------|
| `seed.py` | 📦 Initializes and seeds the MySQL database (`ALX_prodev`) and table (`user_data`). Includes helper functions to create DB, create table, and insert CSV data. |
| `user_data.csv` | 📄 Sample user dataset. Contains UUIDs, names, emails, and ages for seeding the DB. |
| `0-stream_users.py` | 🔁 Defines `stream_users()`, a generator function that yields each user row one by one. Useful for streaming large datasets efficiently. |
| `1-batch_processing.py` | 📦 Contains two functions:<br>• `stream_users_in_batches(batch_size)` – yields data in batches of size `batch_size`.<br>• `batch_processing(batch_size)` – filters and prints users over age 25. |
| `2-lazy_paginate.py` | 📄 Implements paginated access using generators:<br>• `paginate_users(page_size, offset)` – fetches data with `LIMIT/OFFSET`.<br>• `lazy_pagination(page_size)` – lazily yields each page of users as needed. |
| `4-stream_ages.py` | 📊 Memory-efficient average calculation:<br>• `stream_user_ages()` – yields user ages.<br>• `calculate_average_age()` – computes average without using SQL `AVG()`. |
| `0-main.py` | 🧪 Driver to run database setup (connects, creates DB & table, inserts CSV, confirms setup). |
| `1-main.py` | 🧪 Tests `stream_users()` by printing first 6 user rows. |
| `2-main.py` | 🧪 Tests batch processing: filters users older than 25 in chunks. |
| `3-main.py` | 🧪 Tests paginated lazy loading with `lazy_pagination()`. |
| `4-main.py` | 🧪 Tests average age computation using the generator. |
| `README.md` | 📘 This file. Repository and file structure documentation. |

---

## 🧪 What Each File Demonstrates

### `seed.py` – Database Bootstrapping

- Connects to MySQL
- Creates `ALX_prodev` database and `user_data` table (if not exists)
- Reads `user_data.csv` and inserts rows with `INSERT IGNORE`
- Helper functions:
  - `connect_db()`
  - `create_database()`
  - `connect_to_prodev()`
  - `create_table()`
  - `insert_data()`

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

## 🧪 Usage Examples

### Run Database Setup

```bash
$ python3 0-main.py
```

### Stream Users

```bash
$ python3 1-main.py
```

### Process in Batches (Age > 25)

```bash
$ python3 2-main.py | head -n 5
```

### Paginate Users (Lazy)

```bash
$ python3 3-main.py | head -n 10
```

### Compute Average Age

```bash
$ python3 4-main.py
Average age of users: 59.82
```

---

## 🧠 Concepts Reinforced

- Python generator functions and `yield`
- Lazy evaluation and memory optimization
- MySQL `LIMIT` + `OFFSET` pagination
- Data streaming and filtering
- Working with `csv`, `uuid`, and `mysql.connector`

---

## 📎 Dependencies

- Python 3.x
- `mysql-connector-python`:
  ```bash
  pip install mysql-connector-python
  ```

---

## 🔖 License

This repository is maintained for educational purposes by ALX.  
The data and logic are intended for personal learning and backend system design training.

---

## 🙋‍♀️ Author

**Habtamu Tesfaye**  

---
