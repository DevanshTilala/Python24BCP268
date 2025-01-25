def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

def combinations(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def permutations(n, r):
    return factorial(n)/factorial(n-r)

print(combinations(6,5))