def are_anagrams(word1, word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

anagram_check = are_anagrams(word1, word2)
print(anagram_check)
