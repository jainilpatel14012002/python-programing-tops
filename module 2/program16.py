sentence = "I HAVE ONLY LEFT AN YEAR TO COMPLETE MY BTECH IN COMPUTER ENGINEERING HAVE HAVE HAVE"
print(sentence)
d = {}
sum = 1
a = sentence.split()
for i in a:
    if i in d:
     d[i]+=1
    else:
       d[i]=sum
print(d)
