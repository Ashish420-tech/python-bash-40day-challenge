class SalaryError(Exception):
    pass

salary = int(input())

if salary < 15000:
    raise SalaryError("Salary too low")
