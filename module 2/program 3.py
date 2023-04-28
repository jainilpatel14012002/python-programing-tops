# PYTHON PROGRAM TO GET FIBONACCI SERIES OF GIVEN RANGE:
num = int(input("enter the number: "))
a = 0
b = 1
for i in range(1 ,num):
    c = a+b 
    a = b
    b = c
    print(i,c)  