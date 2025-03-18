def length_string(str1):
    if str1=="":  
        return 0
    else:
        return 1+length_string(str1[1:])  

print(length_string("Banana"))
