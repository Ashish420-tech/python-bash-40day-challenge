import os

file = input("Enter File name")
size = os.path.getsize(file)

print("size:", size)
