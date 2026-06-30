age = int(input("Age: "))

if age < 18:
    raise Exception("Age must be above 18")

print("Eligible")
