import os

filename = input("Enter filename: ")

# Check whether the file exists
if not os.path.isfile(filename):
    print("File not found.")
    exit()

print("File exists.\n")

count = 1

# Open input and output files together
with open(filename, "r") as file, open("report.txt", "w") as report:

    for line in file:
        text = f"Employee {count}: {line.strip()}"

        print(text)
        report.write(text + "\n")

        count += 1

    total = count - 1

    print(f"\nTotal Employees: {total}")
    report.write(f"Total Employees: {total}\n")

print("\nReport has been saved to report.txt")
