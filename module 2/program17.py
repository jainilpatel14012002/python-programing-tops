A = input("enter the string: ")
B = "ing"
C = A+B
if len(A)>=3:
 print(C)
if (A.endswith("ing")):
      print(A.replace("ing","ly"))
elif len(A)<3:
      print("Unchanged string is:",A)
