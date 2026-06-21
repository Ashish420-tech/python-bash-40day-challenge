try:
   num= int(input("Enter a number:"))
   result = 100 / num
except Exception as e:
   print(e)

else:
   print("Result:",result)
   
