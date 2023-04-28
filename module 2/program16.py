sentence = "I HAVE ONLY LEFT AN YEAR TO COMPLETE MY BTECH IN COMPUTER ENGINEERING HAVE HAVE HAVE"
d = {}
a = sentence.split()
for i in a:
    c = a.count(i)
    b = d.update(i,c)
    print(b)