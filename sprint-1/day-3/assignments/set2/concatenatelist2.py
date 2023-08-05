list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]
length=len(list1)

for i in range(length):
    for j in range(length):
        list3.append(list1[i]+list2[j])

print(list3)
      