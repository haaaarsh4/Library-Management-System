# Library Management System

## Description
This Python project implements a basic Library Management System using MySQL. It allows users to manage books, employees, customers, issue books, and return books.

## Requirements
Python (3.x)
MySQL Server
MySQL Connector Python (mysql-connector)

## Setup
Install Python: Download Python
Install MySQL Server: Download MySQL Server
Install MySQL Connector Python: `pip install mysql-connector`

## Database Setup
Create a MySQL database named 'LMS'.
Import the provided `library_management_system.sql` file to set up tables.

## Configuration
Update the database connection details in the main function:

## python
Copy code
```c = ms.connect(host="localhost", user='root', password='your_password', database='LMS')```
Replace 'your_password' with your MySQL server password.

## Usage
Run the library_management_system.py script:

## bash
Copy code
python library_management_system.py
Follow on-screen instructions to navigate the Library Management System.

## Features
Book Management: Add, update, display, delete, and search for books.
Employee Management: Add, update, display, delete, and search for employees.
Customer Management: Add, update, display, delete, and search for customers.
Issue a Book: Place an order, update, display, delete, and search for issued books.
Return a Book: Add, update, display, delete, and search for returned books.
Contributions
Contributions are welcome! Open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

