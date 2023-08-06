arr=[2, 7, 11, 15] 
target = 9

i=0
j=len(arr)-1

while i<j:
    if arr[i]+arr[j]==target:
        print(i,j)
        break
    if arr[i]+arr[j]>target:
        j-=1
    else:
        i+=1
