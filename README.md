# 📚 Library Management System

A command-line based **Library Management System** developed in **Python** using **Object-Oriented Programming (OOP)** principles. The application allows users to manage books and members, borrow and return books, search books, and persist data using JSON files.

---

## 🚀 Features

### 📖 Book Management
- Add new books
- Remove books
- View all books
- Search books by title
- Search books by author

### 👤 Member Management
- Register new members
- View all registered members

### 📚 Borrowing System
- Borrow books
- Return books
- Maximum borrow limit (3 books per member)
- Prevent borrowing unavailable books
- Prevent duplicate borrowing of the same book

### 💾 Data Persistence
- Save books to JSON
- Save members to JSON
- Automatically load data when the program starts

### ✅ Testing
- Unit tests written using **pytest**

---

# 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Dataclasses
- Type Hints
- JSON
- Pytest
- Git & GitHub

---

# 📂 Project Structure

```
Library-Management-System/
│
├── main.py
├── books.json
├── members.json
├── README.md
├── requirements.txt
├── .gitignore
│
└── tests/
    └── test_library.py
```

---

# 📦 Requirements

- Python 3.10+
- pytest

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install pytest
```

---

# ▶️ Running the Project

Clone the repository

```bash
git clone <your-repository-link>
```

Move into the project folder

```bash
cd Library-Management-System
```

Run the application

```bash
python main.py
```

---

# 🧪 Running Tests

Run all tests

```bash
pytest -v
```

Example Output

```
============================= test session starts =============================

tests/test_library.py::test_add_book_success PASSED
tests/test_library.py::test_add_duplicate_book PASSED
tests/test_library.py::test_register_member_success PASSED
tests/test_library.py::test_register_duplicate_member PASSED
tests/test_remove_book_success PASSED
tests/test_remove_book_not_found PASSED
tests/test_borrow_book_success PASSED
tests/test_borrow_book_no_copies PASSED
tests/test_return_book_success PASSED
tests/test_search_by_title PASSED

============================== 10 passed ==============================
```

---

# 📋 Menu

```
========= Library Management =========

1. Add Book
2. Remove Book
3. Register Member
4. Borrow Book
5. Return Book
6. Search by Title
7. Search by Author
8. View Books
9. View Members
10. Exit

======================================
```

---

# 🏗️ Project Design

## Book

Attributes

- Book ID
- Title
- Author
- Total Copies
- Available Copies

Methods

- display_details()

---

## Member

Attributes

- Member ID
- Member Name
- Borrowed Books

Methods

- display_details()

---

## Library

Responsibilities

- Add books
- Remove books
- Register members
- Borrow books
- Return books
- Search books by title
- Search books by author
- View books
- View members

---

# 💾 JSON Persistence

The project automatically saves and loads data.

### books.json

Stores

- Book ID
- Title
- Author
- Total Copies
- Available Copies

### members.json

Stores

- Member ID
- Member Name
- Borrowed Books

---

# 📚 Concepts Practiced

This project helped me practice:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Dataclasses
- Type Hints
- Dictionaries
- Lists
- File Handling
- JSON Serialization & Deserialization
- Exception Handling
- Unit Testing with Pytest
- Git & GitHub

---

# 🚧 Future Improvements

Some features that can be added in the future:

- SQLite/PostgreSQL database
- Django Web Application
- Django REST API
- User Authentication
- Book Reservation
- Fine Calculation
- Admin Dashboard
- Book Categories
- Due Date Tracking

---

# 👨‍💻 Author

**Naresh Thota**

B.Tech Computer Science and Engineering

IIITDM Kancheepuram

GitHub: https://github.com/<your-github-username>

---

# ⭐ If you found this project useful, consider giving it a star!