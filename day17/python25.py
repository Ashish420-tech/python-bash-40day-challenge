for num in range(100,500):
   power = len(str(num))
   total = sum(int(d) ** power for d in str(num))
   if total == num:
      print(num)
