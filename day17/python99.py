numbers = [1,2,3,5,99]
n= len(numbers)

missing = sum(range(1,n+1)) - sum(numbers)
print("Missings:", missing)
