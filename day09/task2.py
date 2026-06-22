class Employee:
 
  def __init__(self, name):
       self.name = name
  
  def show(self):
     print("Employee:", self.name)


emp = Employee("Ashish")

emp.show()
