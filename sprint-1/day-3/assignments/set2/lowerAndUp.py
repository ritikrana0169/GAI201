low = ""
upp = ""

def lowerAndUpper(s):
    global low
    global upp
    for x in s:
        if x.islower():
            low += x
        else:
            upp += x
    print(low + upp)

lowerAndUpper("PyNaTive")
