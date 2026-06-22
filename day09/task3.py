class Student:
   

   def __init__(self, name, age):
        self.name= name
        self.age = age

   def info(self):
       print(self.name, self.age)


s = Student("Rahul",22)

s.info()
