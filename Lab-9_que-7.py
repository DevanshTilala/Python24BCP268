def is_palindrome(str1):
    str1=str1.lower()
    if(str1==str1[::-1]):
        return True
    else:
        return False
    
string1=input("Enter a string: ")
print(is_palindrome(string1))