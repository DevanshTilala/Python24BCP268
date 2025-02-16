def fibonacci(n):
    a,b=0,1
    print(f"Fibonacci numbers are: {a} {b}", end=" ")

    for _ in  range(n-2):
        c=a+b
        print(c, end=" ")
        a,b=b,c


n=int(input("Enter number of terms: "))
if(n<=0):
    print("Enter positive number")
elif(n==1):
    print("Fibonacci numbers are: 0")
else:
    fibonacci(n)