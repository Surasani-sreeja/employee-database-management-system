# Employee Database Management System

A Python and MySQL based employee database management project designed to demonstrate database management, CRUD operations, SQL analysis, and Python-MySQL connectivity.

## Features
- View employee records
- Add employees
- Search employees
- Update salary
- Delete employees
- Department-wise employee count and average salary
- Overall salary analysis
- SQL filtering, sorting, grouping and aggregation

## Technologies
- Python
- MySQL
- SQL
- Pandas
- MySQL Connector/Python
- GitHub

## Project Structure
```text
employee-database-management-system/
├── README.md
├── employee_management.py
├── database.sql
├── employees.csv
├── requirements.txt
└── screenshots/
```

## Database
The `database.sql` file creates the `employee_db` database, creates the `employees` table, inserts sample records, and contains analysis queries.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up MySQL
Open MySQL Workbench and run `database.sql`.

### 3. Configure Python
Open `employee_management.py` and replace:
```python
password="YOUR_PASSWORD"
```
with your local MySQL password. Never upload your real password to GitHub.

### 4. Run
```bash
python employee_management.py
```

## SQL Analysis
Examples include:
- Employees earning more than 50,000
- Department-wise employee counts
- Department-wise average salary
- Highest-paid employee
- Minimum, maximum and average salary
- City and joining-date filtering

## Learning Outcomes
- Python database connectivity
- SQL querying and aggregation
- CRUD operations
- Data analysis using Pandas
- Relational database concepts
- Git and GitHub project management

## Future Enhancements
- Add a GUI
- Add authentication
- Add advanced analytics
- Connect the database to a Power BI dashboard
- Generate automated employee reports

## Author
**Surasani Sreeja Reddy**  
B.Tech – Electronics and Communication Engineering  
Aspiring Data Analyst
