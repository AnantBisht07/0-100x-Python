class Employee:
    def __init__(self, salary):
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Invalid salary")
        else:
            self._salary = value


emp = Employee(20000)
emp.salary = -20000
print(f"Employee salary is {emp.salary}")
