try:
    file = open("data.txt")
    number = int(input("Number: "))
    print(100 / number)

except FileNotFoundError:
    print("File not found")

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Wrong input")
