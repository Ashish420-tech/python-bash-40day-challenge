numbers=[1,2,2,3]

inc= all(numbers[i]<= numbers[i+1] for i in range (len(numbers)-1))
dec=all(numbers[i]>= numbers[i+1] for i in range(len(numbers)-1))

print(inc or dec)
