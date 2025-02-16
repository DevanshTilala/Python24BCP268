a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if (a == b == c):
    print("All numbers are equal.")
elif(a>b and a>c):
    print("Largest is",a)
    if(b>c):
        print("Smallest is", c)
    else:
        print("Smallest is", b)
elif(b>a and b>c):
    print("Largest is",b)
    if(a>c):
        print("Smallest is", c)
    else:
        print("Smallest is", a)
else:
    print("Largest is",c)
    if(b>a):
        print("Smallest is", a)
    else:
        print("Smallest is", b)