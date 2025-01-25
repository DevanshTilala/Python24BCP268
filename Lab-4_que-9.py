n=int(input("Enter number of terms: "))
a=0
b=1

print(a, b, end=" ")

c=a+b

while n:
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    n-=1
    