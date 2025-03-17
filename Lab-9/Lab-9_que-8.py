def convert(str1):
    str1=str1.lower()
    words_list=str1.split()
    words_list=' '.join(sorted(list(set(words_list))))
    return words_list

string1=input("Enter a string: ")
print(f"Formatted string is: {convert(string1)}")