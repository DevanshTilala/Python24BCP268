import operator

def frequency(str1):
    words_list=str1.split()
    freq_list={} 
    for i in words_list:
        if i not in freq_list:
            freq_list[i]=1
        else:
            freq_list[i]+=1
    
    freq_list=sorted(freq_list.items())
    return freq_list

string1=input("Enter a string: ") # Example: apple banana orange apple mango banana
print(f"Frequency of words in string is: {frequency(string1)}")