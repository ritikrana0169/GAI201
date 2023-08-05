def is_prime(number):
    if number <= 1:
        return False  
    
    if number <= 3:
        return True   
    
    if number % 2 == 0:
        return False  
    
    
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False  
    
    return True  

input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")
