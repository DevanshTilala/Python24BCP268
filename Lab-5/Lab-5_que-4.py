import random

n=[random.randint(-100,100) for _ in range(30)]
negative_n=[]
positive_n=[]

for i in n:
    if i<0:
        negative_n.append(i)
    else:
        positive_n.append(i)

print(n)
print(positive_n)
print(negative_n)