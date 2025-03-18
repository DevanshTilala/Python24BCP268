def count_vowels(string1, count=0, i=0):
    vowels="aeiouAEIOU"
    if i==len(string1):
        return count
    elif string1[i] in vowels:
        return count + 1 + count_vowels(string1,count,i+1)
    else:
        return count_vowels(string1,count,i+1)

str1=input("Enter a string: ")
print(f"Number of vowels in the string are: {count_vowels(str1)}")