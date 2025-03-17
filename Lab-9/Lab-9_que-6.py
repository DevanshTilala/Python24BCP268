def squares_cubes(n):
    return [(i,i**2,i**3) for i in range(n+1)]

num=int(input("Enter a number: "))
print(f"Series of till given number is: {squares_cubes(5)}")