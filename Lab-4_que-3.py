str=input("Enter a string: ")
count_alp=0
count_num=0

for i in str:
    if i.isalpha():
        count_alp+=1
    elif i.isdigit():
        count_num+=1

print("Numbers are:",count_num,"\nAlphabets are:",count_alp)