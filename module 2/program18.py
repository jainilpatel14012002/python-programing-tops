s = input("enter the string: ")
a = ("not")
b = ("poor")
c = (s.find("not"))
d = (s.find("poor"))
if a and b in s:
    if d-c==4:
        print(s.replace("not poor","good"))
    else:
        print("No changes:",s)
else:
    print("No changes: ",s)