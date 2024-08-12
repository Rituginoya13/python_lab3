class City:
    def __init__(self,city):
        self.city=city
class Company():
    def __init__(self,companyName):
        self.companyName=companyName
class Employee(City,Company):
    def __init__(self, city,name,emp_name,designation,):
        City.__init__(self,city)
        Company.__init__(self,name,)
        self.emp_name=emp_name
        self.designation=designation
        
    def Display(abc):
        print(abc.city)
        print(abc.companyName)
        print(abc.emp_name)
        print(abc.designation)

emp1=Employee("Rajkot","Codex","Ritu","software developer")
emp1.Display()
