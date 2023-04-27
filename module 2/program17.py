A = input("enter the string: ")
B = "ing"
C = A+B
if (A.endswith("ing")):
      print(A.replace("ing","ly"))
elif len(A)<3:
      print("String is Unchanged:",A)
if len(A)>3:
     print(C)
