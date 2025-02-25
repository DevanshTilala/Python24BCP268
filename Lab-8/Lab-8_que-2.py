import random

def num_in_range():
    num=set()
    while(len(num)!=10):
        num.add(random.randint(15,45))
    return num

def count_less_30(n):
    count=0
    for i in n:
        if i<30:
            count+=1
    return count

def delete_more_35(n):
    n=[i for i in n if i<35]
    return set(n)

n=num_in_range()
print(f"Set of numbers between 15 and 45 is: {n}")
print(f"Numbers less than 30 are: {count_less_30(n)}")
print(f"Modifid set is {delete_more_35(n)}")
