import random

rand_list=[random.randint(0,100) for _ in range(20)]
print(rand_list)

check=int(input("Enter a number: "))

for i,n in enumerate(rand_list):
    if(n==check):
        print("Position of given number is", i)
else:
    print(check,"is not in the given list")