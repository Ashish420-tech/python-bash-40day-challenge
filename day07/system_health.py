import os

from datetime import datetime

print("=" * 40)
print("System Health Report")
print("=" * 40)

print("Generated:", datetime.now())

print("\nCurrent Directory:")
print(os.getcwd())


print("\nFiles:")

for file in os.listdir():
    print(file)
