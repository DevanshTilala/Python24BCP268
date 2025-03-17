def count_lower_upper(str1):
    dict1={"UpperCase":0, "LowerCase":0}
    for i in str1:
        if i.isupper():
            dict1["UpperCase"]+=1
        elif i.islower():
            dict1["LowerCase"]+=1
    
    return dict1
    
sample_string=input("Enter a string: ")
print(f"Count of lowercase and uppercase letters is {count_lower_upper(sample_string)}")