def count_lower_upper(str1):
    dict1={"UpperCase":0, "LowerCase":0}
    for i in str1:
        if "A" <= i <= "Z":
            dict1["UpperCase"]+=1
        elif "a" <= i <= "z":
            dict1["LowerCase"]+=1
    
    return dict1
    
sample_string=input("Enter a string: ")
print(count_lower_upper(sample_string))