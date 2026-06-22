class Employee:


   def __init__(self,name,salary):
       self.name= name
       self.salary= salary

   def details(self):
       print("Name:", self.name)
       print("Salary:",self.salary)


emp = Employee("Ashish","500000")

emp.details()
