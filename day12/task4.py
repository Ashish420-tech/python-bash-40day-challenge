class Employee:

    company="ABC Pvt Ltd"

    def __init__(self,name):
        self.name=name


e1=Employee("Ashish")
e2=Employee("Rahul")

print(e1.company)
print(e2.company)
