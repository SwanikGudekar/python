# Define a attribute class with attributr role,department,salary class also has a show detail()method
# create a engineer class that inherits property of employee and has additonal attribute :name and age

class Employee: # parent class

    def __init__ (self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

class Engineer(Employee): # child class

    def __init__(self,name,age,role,department,salary):
        super().__init__(role, department, salary)
        self.name =name
        self.age= age

    
    def showDetail(self):
         print("Name:",self.name)
         print("Age:",self.age)
         print("Role:",self.role)
         print("Department:",self.department)
         print("Salary:",self.salary)
        

e1 = Engineer("swanik",21,"HR","IT",50000)
e1.showDetail()