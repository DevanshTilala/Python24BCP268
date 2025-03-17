def ispangram(str1):
    str1=str1.upper()
    str1=set(str1)
    checkstr={chr(i) for i in range(65,91)}
    if(checkstr.issubset(str1)):
        return True
    else:
        return False
string1="A quick brown fox jumps over the lazy dog"
print(ispangram(string1))