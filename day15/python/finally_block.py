try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File Missing")

finally:
    print("Execution Completed")
