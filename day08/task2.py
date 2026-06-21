try:
   num=int(input("Enter number:"))
   print(100/num)
except ZeroDivisionError:
   print("Cannot Divide by Zero")
   
except 	ValueError:
   print("Please enter only number")
