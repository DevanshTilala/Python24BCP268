def grade(marks):
    if(40<=marks<45):
        print("Grade is P")
    elif(45<=marks<50):
        print("Grade is C")
    elif(50<=marks<55):
        print("Grade is B")
    elif(55<=marks<60):
        print("Grade is B+")
    elif(60<=marks<70):
        print("Grade is A")
    elif(70<=marks<80):
        print("Grade is A+")
    elif(80<=marks<=100):
        print("Grade is O")
    else:
        print("Enter valid marks")

first=int(input("Enter the marks of first subject: "))
second=int(input("Enter the marks of second subject: "))
third=int(input("Enter the marks of third subject: "))

if(first<=39 or second<=39 or third <=39):
    print(f"\nYou failed in the exams!!\n\nTotal marks are {first+second+third}\nYour average is {(first+second+third)/3}\nGrade is F")
else:
    print("\n\nYou passed in the exams\n")
    print(f"Total marks are {first+second+third}")
    print(f"Your average is {(first+second+third)/3}")
    grade((first+second+third)/3)