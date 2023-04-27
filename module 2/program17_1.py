str1 = input("enter the string 1 : ")
str2 = input("enter the string 2 : ")
space =' '
new = str1[0:2]
newstr1 = str1.replace(str1[0:2],str2[0:2])
newstr2 = str2.replace(str2[0:2],new) 

print(newstr1+" "+newstr2)

