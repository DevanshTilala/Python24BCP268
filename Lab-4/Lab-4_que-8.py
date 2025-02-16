n=int(input("Enter a number: "))
print(f"Numbers from {n} to 1 are: ",end="")
for i in range(n, 0, -1):
    print(i, end=" ")