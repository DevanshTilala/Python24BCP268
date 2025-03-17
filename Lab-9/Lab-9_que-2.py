import math

def compute(n):

    # total=0
    # sum=0
    # for i in range(1,n+1):
    #     sum+=n
    #     total+=sum
    #     sum*=10
    # return total
    return n+(n*10 + n)+(n*100 + n*10 + n)+(n*1000 + n*100 + n*10 + n)

# num=int(input("Enter a number: "))
for num in range(4,8):
    print(f"{num} = {compute(num)}")