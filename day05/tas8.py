count=0
with open("employee.txt") as file:
      for line in file:
          count +=1


print("Total Employee:", count)
