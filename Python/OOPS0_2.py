#Employee Payroll

class Employee:
    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_pay(self):
        print(f"This Employee Pay is {self.salary}")

class HourlyEmployee(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours
    
    def calculate_pay(self):
        print(f"This Employee Pay is {self.rate*self.hours}")

employees = [
    FullTimeEmployee(50000),
    HourlyEmployee(100, 20),
    HourlyEmployee(120, 10),
]

for emp in employees:
    emp.calculate_pay()
