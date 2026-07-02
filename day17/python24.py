num = 153
power = len(str(num))
total= sum(int(digit) ** power for digit in str(num))
print("Amstrong" if total == num else "Not Amstrong")
