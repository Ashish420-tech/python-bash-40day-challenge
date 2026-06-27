import os

files= input("Enter file name:")


if os.path.exists(files):
   print("File exists")
else:
  print("Not Found")
