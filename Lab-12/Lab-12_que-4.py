import math as m

class shapes:
    def __init__(self, shape):
        self.x=shape
    def perimeter(self):
        match self.x:
            case 'circle':
                r=float(input("Enter the radius of circle: "))
                peri=2*m.pi*r
                print(f"The perimeter of {self.x} is {peri}")
            case 'square':
                l=float(input("Enter the length of square: "))
                peri=4*l
                print(f"The perimeter of {self.x} is {peri}")
            case 'rectangle':
                l=float(input("Enter the length of square: "))
                b=float(input("Enter the breadth of square: "))
                peri=2*(l+b)
                print(f"The perimeter of {self.x} is {peri}")
    def area(self):
        match self.x:
            case 'circle':
                r=float(input("Enter the radius of circle: "))
                area=m.pi*(r**2)
                print(f"The area of {self.x} is {area}")
            case 'square':
                l=float(input("Enter the length of square: "))
                area=l*l
                print(f"The area of {self.x} is {area}")
            case 'rectangle':
                l=float(input("Enter the length of square: "))
                b=float(input("Enter the breadth of square: "))
                area=l*b
                print(f"The area of {self.x} is {area}")

shape=input("Enter the name of shape: ").lower()
a=shapes(shape)
a.perimeter()
a.area()