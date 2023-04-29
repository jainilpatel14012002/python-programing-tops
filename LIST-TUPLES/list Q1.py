# make a list of number which divisible by 7 and not-divisible by 5 from range 1 to 1000
l1 = []
for i in range(1,1001):
    if(i%7==0 and i%5!=0):
     l1.append(i)
print(l1)

