def prime_factors(num, factors=[],i=2):
    if num<=1:
            return factors
    elif num%i==0:
        factors.append(i)
        return prime_factors(num/i,factors,i)
    else:
        return prime_factors(num,factors,i+1)

# def prime_factors(num, i=2):
#     if num<=1:
#             return []
#     elif num%i==0:
#         return [i]+prime_factors(num/i,i)
#     else:
#         return prime_factors(num,i+1)
    
n=int(input("Enter a number: "))
print(f"Prime factors of given number are: {prime_factors(n)}")

