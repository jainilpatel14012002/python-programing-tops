import random
l1 = []
lucky = []
remove_lucky = []
for i in range(1,100):
    l1.append(i)

for i in range(0,11):
   lucky.append(random.choice(l1))
   l1.remove(lucky[i])
print(l1)
print(lucky)

