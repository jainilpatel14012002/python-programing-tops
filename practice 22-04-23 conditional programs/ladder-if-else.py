print ("ENTER THE AGE OF FIRST : ")
FIRST = input()
print ("ENTER THE AGE OF SECOND : ")
SECOND = input()
print ("ENTER THE AGE OF THIRD : ")
THIRD = input()

if FIRST>=SECOND and FIRST>=THIRD:
    print("oldest is first")
elif SECOND>=FIRST and SECOND>=THIRD:
    print("oldest is second")
elif THIRD>=FIRST and THIRD>=SECOND:
    print("oldest is third")
else:
    print("All are Equal") 