try:
  file = open("demo.txt")

except FileNotFoundError:
   print("File not found")

finally:
   print("Program finished")
