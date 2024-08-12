class Employee:
   def __init__(self,name,dateOfJoin,designation,salary):
        self.name=name
        self.dateOfJoin=dateOfJoin
        self.designation=designation
        self.salary=salary
   def display(abc):
        print("Name:",abc.name)
        print("Date of join :",abc.dateOfJoin)
        print("Designation :",abc.designation)
        print("Salary:",abc.salary)

Emp1=Employee("Ritu","1-1-2024","designer",20000)
Emp1.display()
# Emp2=Employee("Mihir","1-1-2023","Intern",30000)
# Emp2.display()