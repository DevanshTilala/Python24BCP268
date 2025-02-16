def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

def combinations(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def permutations(n, r):
    return factorial(n)/factorial(n-r)

print(f"nCr is: {combinations(6,5)}")
print(f"nPr is: {permutations(6,5)}")