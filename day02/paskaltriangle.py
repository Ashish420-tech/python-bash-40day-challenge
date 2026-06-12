from math import comb
n=6
for i in range(n):
   print(" " * ( n -1), end="")
   for j in range(i + 1):
       print(comb(i,j),end=" ")
   print()
