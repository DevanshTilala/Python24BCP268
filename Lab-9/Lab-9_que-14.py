def count_vowels(string1, count=0, i=0):
    vowels="aeiouAEIOU"
    if string1[i] in vowels:
        return count + count_vowels(string1,count,i+1)
    else:
        return count_vowels(string1,count,i+1)

print(count_vowels("A man a dream a reality"))