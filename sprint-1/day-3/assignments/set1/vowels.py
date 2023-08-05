count=0
def findVowels(str):
 global count
 for x in str:
   if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
      count+=1

 return count
str="hello"
result=findVowels(str)
print(result)