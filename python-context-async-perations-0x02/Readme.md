# 📁 python-context-async-perations-0x02

This project focuses on using **context managers** and **asynchronous programming** with SQLite in Python. It demonstrates how to manage database resources cleanly and perform concurrent operations efficiently using `asyncio` and `aiosqlite`.

---

## 📌 Learning Objectives

- Understand the use of `__enter__` and `__exit__` methods in context managers
- Build reusable class-based context managers for managing database connections
- Execute parameterized SQL queries safely
- Perform asynchronous database operations using `aiosqlite`
- Use `asyncio.gather()` to run multiple coroutines concurrently

---

## 🗂️ Project Structure

```

📂python-context-async-perations-0x02
┣ 📜0-databaseconnection.py
┣ 📜1-execute.py
┗ 📜3-concurrent.py

````

---

## 🔍 File Descriptions

### `0-databaseconnection.py`
Implements a class-based context manager `DatabaseConnection` that handles opening and closing an SQLite database connection automatically.

**Usage:**
```python
with DatabaseConnection("my_database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    ...
````

---

### `1-execute.py`

Implements a reusable context manager `ExecuteQuery` that accepts a query and parameters, then handles both connection and query execution.

**Usage:**

```python
query = "SELECT * FROM users WHERE age > ?"
with ExecuteQuery("my_database.db", query, (25,)) as result:
    ...
```

---

### `3-concurrent.py`

Performs asynchronous database queries using `aiosqlite` and `asyncio.gather()` to fetch all users and users older than 40 concurrently.

**Usage:**

```python
asyncio.run(fetch_concurrently())
```

---

## 🧪 Prerequisites

* Python 3.7+
* SQLite database with a `users` table
* Install dependencies (for async example):

```bash
pip install aiosqlite
```

---

## 🧠 Useful Commands

To create a sample SQLite database for testing:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
```

To insert test data:

```sql
INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 45), ('Charlie', 22);
```
