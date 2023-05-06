a = input("enter the string: ")
b = input("enter the string: ")
new=""
new1=""
d = (len(a)/2)
for i in range(0,len(a)):
    if(i<d):
     new = new+a[i]
    else:
        new1=new1+a[i]
new=new+b+new1
print(new)
