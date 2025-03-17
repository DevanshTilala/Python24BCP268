def ispangram(str1):
    str1=str1.upper()
    str1=set(str1)
    checkstr={chr(i) for i in range(65,91)}
    if(checkstr.issubset(str1)):
        return True
    else:
        return False
string1="Crazy Fredrick bought many very exquisite opal jewels"
if(ispangram(string1)):
    print(f"{string1} is pangram")
else:
    print(f"{string1} is not pangram")