l1 = input("enter the element in list 1: ")
l2 = input("enter the element in list 2: ")
l1=l1.split()
l2=l2.split()
print(l1)
print(l2)
result = False
for i in l1:
    for j in l2:
       if i==j:
         
         result = True
print(result)            