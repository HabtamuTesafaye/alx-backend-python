# Unittests and Integration Tests for ALX Backend Python Project

## Project Overview

This project demonstrates the implementation of **unit tests** and **integration tests** for Python functions and classes, focusing on best practices like **mocking**, **parameterization**, and **fixtures**. It primarily tests a `GithubOrgClient` class that interacts with the GitHub API and utility functions for nested map access and HTTP requests.

---

## Features

- **Unit Tests** for:
  - Utility functions (`access_nested_map`, `get_json`, `memoize`)
  - `GithubOrgClient` methods including `org`, `public_repos`, and license checking.
  
- **Integration Tests** for:
  - End-to-end testing of `GithubOrgClient.public_repos` with fixture data.
  - Mocking external HTTP requests using `unittest.mock.patch`.
  
- Use of **parameterized tests** to test multiple inputs and edge cases cleanly.
- Clear separation between unit and integration tests.
- Use of Python’s built-in `unittest` framework and `parameterized` library.

---

## Requirements

- Python 3.7+
- `requests` library
- `parameterized` library

Install dependencies with:

```bash
pip install requests parameterized
````

---

## File Structure

```
.
├── client.py              # GithubOrgClient implementation and get_json
├── fixtures.py            # JSON fixtures for integration tests
├── test_client.py         # Unit and integration tests for client.py
├── utils.py               # Utility functions like access_nested_map and memoize
├── test_utils.py          # Unit tests for utils.py
└── README.md              # This file
```

---

## Running Tests

Run all tests with:

```bash
python3 -m unittest discover
```

Or run individual test files:

```bash
python3 -m unittest test_client.py
python3 -m unittest test_utils.py
```

---

## Testing Highlights

* **Mocking external calls:** No real HTTP requests are made during tests.
* **Parameterization:** Multiple test scenarios tested elegantly with minimal code.
* **Fixtures:** Realistic sample data used for integration tests to simulate GitHub API responses.

---
