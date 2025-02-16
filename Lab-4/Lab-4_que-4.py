import math

def pythagorean_triplets(n):
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            c=math.sqrt(a**2+b**2)
            if c.is_integer():
                print(a,b,c)

n=30
pythagorean_triplets(n)