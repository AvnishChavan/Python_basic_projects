#A PROGRAM TO CALCULATE PERCENTAGE OF STUDENT WITH IF-ELSE AND DECLARE THE CLASS

print("========Students percentage calculator========")
print("==============================================")

name=str(input("Enter students name:- "))
mark1=float(input("Enter the marks of 1st subject:- "))
mark2=float(input("Enter the marks of 2nd subject:- "))
mark3=float(input("Enter the marks of 3rd subject:- "))

percentage=((mark1+mark2+mark3)/300)*100
print(percentage)

if mark1<=35 or mark2<=35 or mark3<=35:
    print("Failed in one subject.")
else:
    if percentage>75:
        print("Distinction")
    elif percentage>60 and percentage<=75:
        print("First class")
    elif percentage>=40 and percentage<=60:
        print("Second class")
    elif percentage<40:
        print("Fail")