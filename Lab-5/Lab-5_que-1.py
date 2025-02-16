import random

odd_numbers = [random.randrange(1,100,2) for _ in range(5)]
even_numbers = [random.randrange(0,100,2) for _ in range(4)]    

print(odd_numbers)
print(even_numbers)

odd_numbers[2]=even_numbers

print(odd_numbers)

flattened_list=[]

for i in odd_numbers:
    if(type(i)==list):
        for j in i:
            flattened_list.append(j)
    else:
        flattened_list.append(i)

flattened_list.sort()
print(flattened_list)