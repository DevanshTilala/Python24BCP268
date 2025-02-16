a=float(input("Enter length of rectangle: "))
b=float(input("Enter breadth of rectangle: "))

area=a*b
peri=2*(a+b)

if(area>peri):
    print("Area:",area,"is greater than perimeter:",peri)
else:
    print("Area:",area,"is not greater than perimeter:",peri)