import os

for file in os.listdir("."):
    print(file)


count = len(os.listdir("."))

print("Total files:", count)
