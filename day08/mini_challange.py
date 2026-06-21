

file = input("Enter a file name:")
try:
  file1 = open(file)
  line_count = 0
  for line in file1:
     print(line, end="")
     line_count +=1
  file1.close()
  
  print("Number of line:",line_count)

except FileNotFoundError:
  print("File not found")

