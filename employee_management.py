import mysql.connector
import pandas as pd


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="employee_db"
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database.")

        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None


def view_employees(connection):
    query = "SELECT * FROM employees"
    df = pd.read_sql(query, connection)
    print("\nEmployee Records")
    print(df.to_string(index=False))


def add_employee(connection):
    cursor = connection.cursor()

    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    salary = float(input("Enter Salary: "))
    joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
    city = input("Enter City: ")

    query = """
    INSERT INTO employees
    (employee_id, name, gender, age, department, designation, salary, joining_date, city)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (employee_id, name, gender, age, department,
              designation, salary, joining_date, city)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Employee added successfully.")
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()


def search_employee(connection):
    employee_id = int(input("Enter Employee ID: "))

    query = "SELECT * FROM employees WHERE employee_id = %s"
    df = pd.read_sql(query, connection, params=(employee_id,))

    if df.empty:
        print("Employee not found.")
    else:
        print(df.to_string(index=False))


def update_salary(connection):
    cursor = connection.cursor()

    employee_id = int(input("Enter Employee ID: "))
    new_salary = float(input("Enter New Salary: "))

    query = "UPDATE employees SET salary = %s WHERE employee_id = %s"

    try:
        cursor.execute(query, (new_salary, employee_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Salary updated successfully.")
        else:
            print("Employee not found.")
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()


def delete_employee(connection):
    cursor = connection.cursor()

    employee_id = int(input("Enter Employee ID: "))

    query = "DELETE FROM employees WHERE employee_id = %s"

    try:
        cursor.execute(query, (employee_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()


def department_analysis(connection):
    query = """
    SELECT department,
           COUNT(*) AS employee_count,
           ROUND(AVG(salary), 2) AS average_salary
    FROM employees
    GROUP BY department
    ORDER BY average_salary DESC
    """

    df = pd.read_sql(query, connection)
    print("\nDepartment Analysis")
    print(df.to_string(index=False))


def salary_analysis(connection):
    query = """
    SELECT MIN(salary) AS minimum_salary,
           MAX(salary) AS maximum_salary,
           ROUND(AVG(salary), 2) AS average_salary
    FROM employees
    """

    df = pd.read_sql(query, connection)
    print("\nSalary Analysis")
    print(df.to_string(index=False))


def main():
    connection = create_connection()

    if connection is None:
        return

    while True:
        print("\n" + "=" * 45)
        print("EMPLOYEE DATABASE MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. View Employees")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Department Analysis")
        print("7. Salary Analysis")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_employees(connection)
        elif choice == "2":
            add_employee(connection)
        elif choice == "3":
            search_employee(connection)
        elif choice == "4":
            update_salary(connection)
        elif choice == "5":
            delete_employee(connection)
        elif choice == "6":
            department_analysis(connection)
        elif choice == "7":
            salary_analysis(connection)
        elif choice == "8":
            print("Thank you for using Employee Database Management System.")
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
