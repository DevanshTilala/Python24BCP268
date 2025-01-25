def slope(x1,y1,x2,y2):
    if x2 - x1 == 0:
        return float('inf')
    m=(y2-y1)/(x2-x1)
    return m
 
x1=int(input("Enter x-coordinate of first point: "))
y1=int(input("Enter y-coordinate of first point: "))
x2=int(input("Enter x-coordinate of second point: "))
y2=int(input("Enter y-coordinate of second point: "))
x3=int(input("Enter x-coordinate of third point: "))
y3=int(input("Enter y-coordinate of third point: "))

if(slope(x1,y1,x2,y2)==slope(x2,y2,x3,y3)):
    print("All points fall on a straight line")
else:
    print("Points are not in a straight line")