# string functions
# len() function --> this function returns length of string
S = "jainil patel"
print(len(S)) 

# string.endswith(" ") --> this function returns boolean value if string ends with space then it returns true else false
Z = "PATEL JAINIL"
S = Z.endswith("NIL")
print(S)

# string.count("") --> it counts the total number of occurence of any character
B = "i am learning the python language at tops techonologies"
n = B.count('a')
print(n) 

# string.capitalize() --> this will capitalize the first letter of given String
C = "jainil"
c = C.capitalize()
print(c)

# string.find() --> this will find a word and return index of first occurence of word
D = "tops is good learning career center in ahmedabad for new technologies"
d = D.find("good")
print(d)

# string.replace(oldword,new word) --> this function replace old-word with new-word
E = "tops is good learning career center in ahmedabad for new technologies"
e = E.replace('ahmedabad','vadodara')
print(e)