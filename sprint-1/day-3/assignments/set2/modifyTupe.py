tuple1 = (11, [22, 33], 44, 55)

new_list = list(tuple1)  
new_list[1][0] = 222     

modified_tuple = tuple(new_list)

print("tuple1:", modified_tuple)
