arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(len(arr) - 1): 
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
