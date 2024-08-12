class Company:
    def __init__(self,name,city,mobNo):
        self.name=name
        self.city=city
        self.mobNo=mobNo
class Employee(Company):
    def __init__(self, name, city, mobNo,emp_name,designation,salary):
        super().__init__(name, city, mobNo)
        self.emp_name=emp_name
        self.designation=designation
        self.salary=salary
    def Display(abc):
        print(abc.name)
        print(abc.city)
        print(abc.mobNo)
        print(abc.emp_name)
        print(abc.designation)
        print(abc.salary)    

Emp1=Employee("codex","Rajkot",7567845501,"ritu","software developer",482748)
Emp1.Display()
        