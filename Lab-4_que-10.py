import math

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

def sin_function(x):
    result=0
    sign=1

    for n in range(1, 10, 2):
        result+=(x*sign)**n/factorial(n)
        sign*=-1

    return result

x=float(input("Enter the angle in degrees[0-360]: "))
x*=(3.14159/180)
sin_x = x - (x**3/factorial(3)) +  (x**5/factorial(5)) - (x**7/factorial(7))
print(sin_function(x))
print(sin_x)
print(math.sin(x))