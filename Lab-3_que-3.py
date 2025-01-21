string1=input("Enter a string: ")
string2=input("Enter another string: ")

if string1 in string2:
    print(string1,"is present in",string2)
elif string2 in string1:
    print(string2,"is present in",string1)
else:
    print("No string is present in neither")