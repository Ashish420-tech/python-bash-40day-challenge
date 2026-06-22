class Car:
   
  def __init__(self, brand):
      self.brand = brand

  def show(self):
       print(self.brand)



c1= Car("Toyota")
c2= Car("Tesla")

c1.show()
c2.show()
