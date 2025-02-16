a=int(input("Enter your age: "))

if(a>0 and a<150):
    if(a<18):
        print("Minor")
    else:
        print("Major")
else:
    print("Please enter valid age")