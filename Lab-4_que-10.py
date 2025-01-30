import math

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

def sin_function(x):
    result=0
    sign=1

    if(x==math.pi):
        return 0.0
    
    for n in range(1, 20, 2):
        result+=sign*(x**n)/factorial(n)
        sign*=-1

    return result

angle_deg=float(input("Enter the angle in degrees: "))
angle_deg%=360
angle_rad=(angle_deg*math.pi)/180
# sin_x = x - (x**3/factorial(3)) +  (x**5/factorial(5)) - (x**7/factorial(7))
print(f"Sin value by formula: {sin_function(angle_rad)}")
# print(sin_x)
print(f"Sin value by inbuilt function: {math.sin(angle_rad)}")