class Employee:
    def __init__(self, name, Department, salary):
        self.name = name
        self.Department = Department 
        self.salary = salary

    def display_salary_report(self):
        print(f"Name: {self.name}\nDepartment: {self.Department}\nSalary: ${self.salary}\n")


class SalaryReport:
    def __init__(self, employees):
        self.employees = employees

    def generate_report(self):
        print("Salary Report:")
        for employee in self.employees:
            employee.display_salary_report()


# Example Usage:
employee1 = Employee("Ali Raza", "Software Engineer", 75000)

employees_list = [employee1]

salary_report = SalaryReport(employees_list)
salary_report.generate_report()