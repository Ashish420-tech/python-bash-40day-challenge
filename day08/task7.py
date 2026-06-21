try:
  a = int(input("First number:"))
  b = int(input("Second number:"))

  print(a/b)

except ZeroDivisionError:
  print("Cannot divide by zero:")
