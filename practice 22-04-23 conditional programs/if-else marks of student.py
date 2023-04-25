subject1 = int(input("enter the marks of subject 1:"))
subject2 = int(input("enter the marks of subject 2:"))
subject3 = int(input("enter the marks of subject 3:"))
percentage = (subject1+subject2+subject3)*100/300
if percentage>90:
    print("you got A+ ranking")
elif percentage>80:
        print("you got A ranking")
elif percentage>70:
            print("you got B+ ranking")
elif percentage>50:
                print("you got B ranking")
elif percentage<40 and percentage>30:
                    print("you got C+ ranking")
else:
                  print("you are failed")
                
