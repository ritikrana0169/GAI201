def displayList(num):
    for x in num:
        if x%5==0:
            if x>150 and x<=500:
                continue
            if x>500:
                break
            else:
                print(x)

numbers = [12, 75, 150, 180, 145, 525, 50]
displayList(numbers)