import math as m

class solids:
    def __init__(self,solid):
        self.data=solid
    def surface_area(self):
        match self.data:
            case 'sphere':
                r=float(input("Enter the radius of sphere: "))
                area=4*m.pi*(r**2)
                print(f"The surface area of {self.data} is {area}")
            case 'cylinder':
                r=float(input("Enter the radius of cylinder: "))
                c=float(input("Enter the height of cylinder: "))
                area=2*m.pi*r*c
                print(f"The surface area of {self.data} is {area}")
            case 'cube':
                a=float(input("Enter the length of cube: "))
                area=6*(a**2)
                print(f"The surface area of {self.data} is {area}")
            case 'cuboid':
                a=float(input("Enter the length of cuboid: "))
                b=float(input("Enter the breadth of cuboid: "))
                c=float(input("Enter the height of cuboid: "))
                area=2*(a*b + b*c + c*a)
                print(f"The surface area of {self.data} is {area}")
            case _:
                print("Enter the valid solid name")
    def volume(self):
        match self.data:
            case 'sphere':
                r=float(input("Enter the radius of sphere: "))
                volume=4*m.pi*(r**3)/3
                print(f"The volume of {self.data} is {volume}")
            case 'cylinder':
                r=float(input("Enter the radius of cylinder: "))
                c=float(input("Enter the height of cylinder: "))
                volume=m.pi*(r**2)*c
                print(f"The volume of {self.data} is {volume}")
            case 'cube':
                a=float(input("Enter the length of cube: "))
                volume= a**3
                print(f"The volume of {self.data} is {volume}")
            case 'cuboid':
                a=float(input("Enter the length of cuboid: "))
                b=float(input("Enter the breadth of cuboid: "))
                c=float(input("Enter the height of cuboid: "))
                volume=a*b*c
                print(f"The volume of {self.data} is {volume}")
            case _:
                print("Enter the valid solid name")

shape=input("Enter the name of solid: ").lower()
a=solids(shape)
a.surface_area()
a.volume()