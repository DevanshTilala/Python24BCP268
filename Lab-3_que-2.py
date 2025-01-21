def toggle_case(string):

    newstring=''

    for i in string:
        if 'a'<=i<='z':
            newstring+=chr(ord(i)-32)
        elif 'A'<=i<='Z':
            newstring+=chr(ord(i)+32)
        else:
            newstring+=i
    
    return newstring

def upper_case(string):
    newstring=''

    for i in string:
        if 'a'<=i<='z':
            newstring+=chr(ord(i)-32)
        else:
            newstring+=i
    
    return newstring

def lower_case(string):

    newstring=''

    for i in string:
        if 'A'<=i<='Z':
            newstring+=chr(ord(i)+32)
        else:
            newstring+=i
    
    return newstring

str=input("Enter a string: ")
print(lower_case(str))