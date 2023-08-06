arr = [64, 25, 12, 22, 11]

for x in range(len(arr)):
    minIndex = x
    for y in range(x + 1, len(arr)):
        if arr[y] < arr[minIndex]:
            minIndex = y
            
   
    arr[x], arr[minIndex] = arr[minIndex], arr[x]

print(arr)
