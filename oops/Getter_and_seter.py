class employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

emp = employee()
print(emp.get_salary())  # Accessing salary using getter
emp.set_salary(60000)    # Modifying salary using setter
print(emp.get_salary())