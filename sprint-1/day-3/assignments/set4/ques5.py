def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  
    
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    
    return missing_number

input_nums = [3, 0, 1,2]
output = find_missing_number(input_nums)
print(output)
