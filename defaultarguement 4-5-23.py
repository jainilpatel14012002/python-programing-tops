# * --> is denoted as tuple
# ** --> is denoted as dictionary

def test(a=40,b=30,c=20,d=10):
    print("A :",a,"B :",b,"C :",c,"D :",d)
test(b=20)

def new(a,b,c,*d):
    print("A :",a,"B :",b,"C :",c,"D :",d)
new(6,7,9,10,11,12)

def dictionary(a,b,c,*d,**e):
    print("A :",a,"B :",b,"C :",c,"D :",d,"E :",e)

dictionary(5,7,3,6,6,3,5,x=5,y=55,z=9)


