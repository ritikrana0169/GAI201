def string_permutations(input_str):
    if len(input_str) == 0:
        return []
    if len(input_str) == 1:
        return [input_str]
    
    permutations = []
    for i in range(len(input_str)):
        char = input_str[i]
        remaining_chars = input_str[:i] + input_str[i+1:]
        for perm in string_permutations(remaining_chars):
            permutations.append(char + perm)
    
    return permutations

input_str = "abc"
output = string_permutations(input_str)
print(output)
