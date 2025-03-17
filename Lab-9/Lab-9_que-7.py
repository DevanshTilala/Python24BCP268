def is_palindrome(str1):
    if(str1==str1[::-1]):
        return True
    else:
        return False
    # return str1, str1[::-1]
    
string1=input("Enter a string: ")
if is_palindrome(string1):
    print(f"{string1} is palindrome")
else:
    print(f"{string1} is not palindrome")