import random

n=[random.randint(1,31) for _ in range(50)]

print(n)

for i in n:
    if n.count(i)>1:
        n=[x for x in n if x!=i]
        n.append(i)

print(n)