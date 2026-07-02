arr =[64,25,12,22]

for i in range(len(arr)):
    min_i =i
    for j in range(i +1,len(arr)):
        if arr[j] < arr[min_i]:
             min_i=j
    arr[i], arr[min_i] = arr[min_i], arr[i]


print(arr)
