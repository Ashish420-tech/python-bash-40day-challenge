try:

  file= open("sample.txt")
  
except FileNotFoundError:
   print("File is not found")
