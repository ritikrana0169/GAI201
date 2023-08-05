def printPattern(num):
    for x in range(1,num+1):
        bag=""
        for y in range(1,x+1):
            bag+=str(y)+" "
        print(bag)



printPattern(5)