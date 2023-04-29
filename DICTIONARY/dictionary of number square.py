# dictionary of value is equal to value*value
a = {}
num = int(input("enter the number : "))
z = num*num
for i in range(1,num+1):
    a[i] = i*i
print(a)