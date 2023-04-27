# list sort()
l1 = [2,2,3,42,32,3,32]
l1.sort()
print(l1)

# list reverse() --> it will reverse the reverse
l2 = [1,4,8,9,4,3,1]
l2.reverse()
print(l2)

# list append() --> it will add element at end of list
l3 = [1,2,3,4,5,6]
l3.append(2500)
print(l3)

# list insert() --> it will insert element in the list
l4 = [1,4,0,1,2,0,0,2]
l4.insert(0,"JAINIL PATEL's BIRTHDAY ")
print(l4)

# list pop() --> it will pop out the element st particular index
l5 = [1,5,2,3,9,1,3]
l5.pop(5)
print(l5)

# list remove() --> it will remove the element from the list as user enters
l6 = [1,2,3,4,5,6]
l6.remove(3)
print(l6)

# list extend() --> it will add a new list in the previous list 
l7 = ['jainil','darshan','jhanvi','vishal']
l8 = [1,2,3,4,5]
l7.extend(l8)
print(l7)

# list.index() --> it will show the index of particular element
l9 = [6,8,1,3,4,6,5,3]
a = l9.index(5)
print(a)