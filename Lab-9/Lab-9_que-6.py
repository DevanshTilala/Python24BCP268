def squares_cubes(n):
    lst=[(i,i**2,i**3) for i in range(n+1)]
    return lst

print(squares_cubes(5))