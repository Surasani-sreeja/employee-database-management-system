CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    age INT,
    department VARCHAR(50),
    designation VARCHAR(100),
    salary DECIMAL(10,2),
    joining_date DATE,
    city VARCHAR(50)
);

INSERT INTO employees
(employee_id, name, gender, age, department, designation, salary, joining_date, city)
VALUES
(101, 'Rahul Sharma', 'Male', 25, 'IT', 'Software Engineer', 55000, '2023-06-15', 'Hyderabad'),
(102, 'Priya Reddy', 'Female', 24, 'HR', 'HR Executive', 42000, '2023-08-10', 'Bangalore'),
(103, 'Arjun Kumar', 'Male', 28, 'Finance', 'Financial Analyst', 60000, '2022-04-20', 'Chennai'),
(104, 'Sneha Rao', 'Female', 26, 'IT', 'Data Analyst', 58000, '2023-01-12', 'Hyderabad'),
(105, 'Kiran Patel', 'Male', 30, 'Sales', 'Sales Executive', 45000, '2021-11-05', 'Mumbai'),
(106, 'Anjali Singh', 'Female', 27, 'Marketing', 'Marketing Analyst', 52000, '2022-07-18', 'Pune'),
(107, 'Vikram Reddy', 'Male', 29, 'IT', 'Senior Developer', 75000, '2020-09-25', 'Hyderabad'),
(108, 'Meena Das', 'Female', 25, 'Finance', 'Accountant', 48000, '2023-03-14', 'Kolkata'),
(109, 'Rohit Verma', 'Male', 31, 'Sales', 'Sales Manager', 70000, '2019-12-10', 'Delhi'),
(110, 'Divya Nair', 'Female', 26, 'HR', 'Recruiter', 46000, '2022-10-21', 'Bangalore'),
(111, 'Sanjay Kumar', 'Male', 27, 'IT', 'Backend Developer', 62000, '2021-05-17', 'Hyderabad'),
(112, 'Pooja Shah', 'Female', 29, 'Marketing', 'Marketing Manager', 68000, '2020-02-11', 'Mumbai'),
(113, 'Naveen Reddy', 'Male', 24, 'IT', 'Junior Developer', 40000, '2024-01-08', 'Hyderabad'),
(114, 'Lakshmi Rao', 'Female', 32, 'Finance', 'Finance Manager', 78000, '2018-06-19', 'Chennai'),
(115, 'Amit Joshi', 'Male', 28, 'Sales', 'Sales Executive', 44000, '2022-09-23', 'Pune');

-- Analysis queries
SELECT * FROM employees;
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'IT';
SELECT * FROM employees ORDER BY salary DESC;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MAX(salary) AS maximum_salary FROM employees;
SELECT MIN(salary) AS minimum_salary FROM employees;
SELECT department, COUNT(*) AS employee_count FROM employees GROUP BY department;
SELECT department, ROUND(AVG(salary), 2) AS average_salary FROM employees GROUP BY department;
SELECT * FROM employees ORDER BY salary DESC LIMIT 1;
SELECT * FROM employees WHERE city = 'Hyderabad';
SELECT * FROM employees WHERE joining_date >= '2022-01-01';
SELECT * FROM employees WHERE gender = 'Female';
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;
