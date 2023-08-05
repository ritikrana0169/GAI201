sum = 1
def factorial(num):
    global sum
    for x in range(1, num + 1):
        sum *= x
    return sum
    
result=factorial(5)
print(result)

