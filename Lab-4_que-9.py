n=int(input("Enter number of terms: "))
a,b=0,1

print(f"Fibonacci numbers are: {a} {b}", end=" ")

while n-2:
    c=a+b
    print(c, end=" ")
    a=b
    b=c
    n-=1
    