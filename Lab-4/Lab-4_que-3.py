def count_alph_num(str):
    alphabets=0
    numbers=0
    for i in str:
        if i.isalpha():
            alphabets+=1
        elif i.isdigit():
            numbers+=1
    return alphabets,numbers

str=input("Enter a string: ")
count_alp,count_num=count_alph_num(str)
print("Numbers are:",count_num,"\nAlphabets are:",count_alp)