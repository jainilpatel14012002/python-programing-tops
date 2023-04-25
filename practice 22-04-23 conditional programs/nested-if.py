# program to find largest number among all three numbers
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a>b:
    print("a is greater than b")
    if a>c:
        print("a is greater than c")
    else:
        print("a is not greater than c")

else:
    print("a is not greater than b and c")

        