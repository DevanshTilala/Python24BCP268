def count_alpha_digits(str1):
    alpha_num_count={'alphabets':0, 'numbers':0}

    for i in str1:
        if i.isalpha():
            alpha_num_count['alphabets']+=1
        elif i.isdigit():
            alpha_num_count['numbers']+=1
    
    return alpha_num_count

string1=input("Enter a string: ")
print(f"The number of alphabets and digits in string is: {count_alpha_digits(string1)}")