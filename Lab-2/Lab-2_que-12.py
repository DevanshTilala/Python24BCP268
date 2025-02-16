import math

x=int(input("Enter the x-coordinate of center: "))
y=int(input("Enter the y-coordinate of center: "))
r=int(input("Enter the radius of circle: "))
x1=int(input("Enter the x-coordinate of point: "))
y1=int(input("Enter the y-coordinate of point: "))

r1=math.sqrt(math.pow(x-x1,2) + math.pow(y-y1,2))

if(r1<r):
    print("Point is inside the circle")
elif(r1==r):
    print("Point is on the circle")
else:
    print("Point is outside the circle")