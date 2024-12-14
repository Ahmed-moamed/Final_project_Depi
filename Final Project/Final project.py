import csv


class Employee:
    # counter to count number of employee (addition)
    num_employee = 0

    def __init__(self, ID_emp, Name, Position, Salary, Email):
        self.ID = int(ID_emp)
        self.Name = str(Name)
        self.Position = str(Position)
        self.Salary = float(Salary)
        self.Email = (str)
        Employee.num_employee += 1

    # methods of Employee class
    def update_emp_data(self, Name=None, Position=None, Salary=None, Email=None):
        if Name:
            self.Name = str(Name)
        if Position:
            self.Position = str(Position)
        if Salary:
            self.Salary = float(Salary)
        if Email:
            self.Email = str(Email)


class EmployeeManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.employees = self.load_data()

    # methods of EmployeeManager class
    def load_data(self):
        # create empty dictionary to save data in it
        employees_dict = {}
        try:
            with open(self.file_name, 'r') as file:
                # >> The keys in this dictionary correspond to the column headers in the CSV file,
                # >> and the values are the respective data for each row.
                csv_reader = csv.DictReader(file)
                for Row in csv_reader:
                    obj_empl = Employee(
                        ID_emp=Row['Employee ID'],
                        Name=Row['Employee Name'],
                        Position=Row['Employee Position'],
                        Salary=Row['Employee Salary'],
                        Email=Row['Employee Email']
                    )

                    # we save the data of Employee objects in the dictionary employees
                    # and the keys of the values is standard >> ID
                    # he Employee object encapsulates all relevant information about an employee in a structured way.
                    employees_dict[obj_empl.ID] = obj_empl

        except FileNotFoundError:
            print('This file not founded , please try again with new file')
        return employees_dict



import csv

# Define the Employee class to represent individual employee records.
class Employee:
    """Represents a single employee with basic attributes."""

    def __init__(self, emp_id, name, position, salary, email):
        """
        Initializes an Employee instance.

        Args:
            emp_id (str): Unique employee ID.
            name (str): Name of the employee.
            position (str): Job position/title.
            salary (float): Employee's salary.
            email (str): Employee's email address.
        """
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        """
        Updates one or more attributes of the employee.

        Args:
            name (str, optional): New name of the employee.
            position (str, optional): New job position.
            salary (float, optional): New salary value.
            email (str, optional): New email address.
        """
        if name:
            self.name = name
        if position:
            self.position = position
        if salary:
            self.salary = salary
        if email:
            self.email = email


# Define the EmployeeManager class to handle employee operations.
class EmployeeManager:
    """Manages the main operations of the Employee Management System."""

    def __init__(self, filename):
        """
        Initializes the EmployeeManager instance.

        Args:
            filename (str): Name of the CSV file storing employee data.
        """
        self.filename = filename
        # Load employee data from the CSV file.
        self.employees = self.load_data()

    def load_data(self):
        """
        Loads employee data from a CSV file.

        Returns:
            dict: A dictionary of employees with emp_id as keys.
        """
        employees = {}
        try:
            with open(self.filename,"r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Create Employee objects and store them in the dictionary.
                    emp = Employee(
                        emp_id=row['ID'],
                        name=row['Name'],
                        position=row['Position'],
                        salary=float(row['Salary']),
                        email=row['Email']
                    )
                    employees[emp.emp_id] = emp
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with an empty database.")
        return employees

    def save_data(self):
        """
        Saves employee data to a CSV file.
        """
        with open(self.filename, mode="w", newline="") as file:
            fieldnames = ['ID', 'Name', 'Position', 'Salary', 'Email']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in self.employees.values():
                writer.writerow({
                    'ID': emp.emp_id,
                    'Name': emp.name,
                    'Position': emp.position,
                    'Salary': emp.salary,
                    'Email': emp.email
                })

    def add_employee(self, emp):
        """
        Adds a new employee to the system.

        Args:
            emp (Employee): The Employee object to be added.

        Returns:
            bool: True if added successfully, False if already exists.
        """
        if emp.emp_id in self.employees:
            print("Employee already exists!")
            return False
        self.employees[emp.emp_id] = emp
        self.save_data()
        print("Employee added successfully!")
        return True

    def update_employee(self, emp_id, **kwargs):
        """
        Updates an existing employee's details.

        Args:
            emp_id (str): The ID of the employee to update.
            kwargs: Attributes to update (e.g., name, position).

        Returns:
            bool: True if updated successfully, False if employee not found.
        """
        if emp_id not in self.employees:
            print("Employee not found!")
            return False
        self.employees[emp_id].update_details(**kwargs)
        self.save_data()
        print("Employee updated successfully!")
        return True

    def delete_employee(self, emp_id):
        """
        Deletes an employee from the system.

        Args:
            emp_id (str): The ID of the employee to delete.

        Returns:
            bool: True if deleted successfully, False if employee not found.
        """
        if emp_id not in self.employees:
            print("Employee not found!")
            return False
        del self.employees[emp_id]
        self.save_data()
        print("Employee deleted successfully!")
        return True

    def search_employee(self, emp_id):
        """
        Searches for an employee by their ID.

        Args:
            emp_id (str): The ID of the employee to search.

        Returns:
            Employee or None: The Employee object if found, else None.
        """
        return self.employees.get(emp_id, None)

    def list_employees(self):
        """
        Lists all employees in the system.
        """
        if not self.employees:
            print("No employees registered.")
            return
        for emp in self.employees.values():
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Position: {emp.position}, "
                  f"Salary: {emp.salary}, Email: {emp.email}")


# Main function to run the program.
def main():
    manager = EmployeeManager("employees.csv")

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = float(input("Enter Employee Salary: "))
            email = input("Enter Employee Email: ")
            emp = Employee(emp_id, name, position, salary, email)
            manager.add_employee(emp)

        elif choice == "2":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (or press Enter to skip): ")
            position = input("Enter new Position (or press Enter to skip): ")
            salary = input("Enter new Salary (or press Enter to skip): ")
            email = input("Enter new Email (or press Enter to skip): ")
            manager.update_employee(
                emp_id,
                name=name or None,
                position=position or None,
                salary=float(salary) if salary else None,
                email=email or None
            )

        elif choice == "3":
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)

        elif choice == "4":
            emp_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee(emp_id)
            if emp:
                print(f"ID: {emp.emp_id}, Name: {emp.name}, Position: {emp.position}, "
                      f"Salary: {emp.salary}, Email: {emp.email}")
            else:
                print("Employee not found.")

        elif choice == "5":
            manager.list_employees()

        elif choice == "6":
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid option. Please try again.")


# Entry point of the program.
if __name__ == "__main__":
    main()
