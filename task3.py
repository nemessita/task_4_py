class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

    def calculate_emp_salary(self, hours_worked):
        if hours_worked <= 50:
            return self.emp_salary
        else:
            overtime_hours = hours_worked - 50
            overtime_amount = (overtime_hours * (self.emp_salary / 50))
            total_salary = self.emp_salary + overtime_amount
            return total_salary


employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")


employee1.print_employee_details()
employee1.assign_department("HR")
print(f"Updated Department: {employee1.emp_department}")
new_salary = employee1.calculate_emp_salary(60)
print(f"New Salary with Overtime: ${new_salary}")
