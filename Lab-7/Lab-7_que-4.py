str="Hello hi how are you"
char_dict={}
for i in str:
    if i not in char_dict:
        char_dict[i]=1
    else:
        char_dict[i]+=1

print(f"Frequency of characters in string is: {char_dict}")