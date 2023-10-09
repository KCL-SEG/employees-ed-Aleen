"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
    
class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus_commission=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.monthly_salary + self.bonus_commission

    def __str__(self):
        if self.bonus_commission > 0:
            return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked, commission_per_contract=0, contracts_landed=0):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.contracts_landed = contracts_landed

    def get_pay(self):
        hourly_pay = self.hourly_wage * self.hours_worked
        commission_pay = self.commission_per_contract * self.contracts_landed
        return hourly_pay + commission_pay

    def __str__(self):
        if self.commission_per_contract > 0:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."


class HourlyEmployeeWithBonus(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus_commission=0):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission

    def get_pay(self):
        hourly_pay = self.hourly_wage * self.hours_worked
        return hourly_pay + self.bonus_commission

    def __str__(self):
        return f"{self.name} works on an hourly contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."






# Create employee objects
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
renee = SalaryEmployee('Renee', 3000, bonus_commission=800)
jan = HourlyEmployee('Jan', 25, 150, commission_per_contract=220, contracts_landed=3)
robbie = SalaryEmployee('Robbie', 2000, bonus_commission=1500)
ariel = HourlyEmployeeWithBonus('Ariel', 30, 120, 600)

# Test the get_pay and __str__ methods
print(billie.get_pay())  # Should return 4000
print(str(billie))  # Should print the expected string
print(charlie.get_pay())  # Should return 2500
print(str(charlie))  # Should print the expected string
print(renee.get_pay())  # Should return 3800
print(str(renee))  # Should print the expected string
print(jan.get_pay())  # Should return 4410
print(str(jan))  # Should print the expected string
print(robbie.get_pay())  # Should return 3500
print(str(robbie))  # Should print the expected string
print(ariel.get_pay())  # Should return 4200
print(str(ariel))  # Should print the expected string