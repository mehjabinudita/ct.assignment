x = int(input())

if x>=90 and x<=100:
    print("Grade is A")
elif x>=80 and x<=89:
    print("Grade is B")
elif x>=70 and x<=79:
    print("Grade is C")
elif x>=60 and x<=69:
    print("Grade is D")
elif x<60:
    print("Grade is F")
elif x<0 and x>100:
    print("Error, please enter numeric input between 0 and 100")
    