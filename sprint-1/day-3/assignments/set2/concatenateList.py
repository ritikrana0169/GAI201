list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

length=min(len(list1),len(list2))
for x in range(length):
    list1[x]+=list2[x]


print(list1)
