l1 = [1,2,3,2,1,4,5,6]
l2 = []
for i in l1:
    if i in l2:
        l1.remove(i)
    else:
        l2.append(i)
print(l2)