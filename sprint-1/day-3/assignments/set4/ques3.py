def longest_common_prefix(strs):
    if not strs:
        return ""
    
   
    min_len = min(len(s) for s in strs)
    
    common_prefix = ""
    
    for i in range(min_len):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            common_prefix += char
        else:
            break
    
    return common_prefix

input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)  
