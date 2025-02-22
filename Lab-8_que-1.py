def word_to_upper(string):
    string_set=set()

    for i in string:
        temp_string=""
        for j in i:
            # if 'A' <= j <= 'Z':
            #     j=chr(ord(j)+32)
            #     temp_string+=j
            if 'a' <= j <= 'z':
                j=chr(ord(j)-32)
                temp_string+=j
            else:
                temp_string+=j
        string_set.add(temp_string)

    return string_set

string=["Devansh","Prince","abcd","efgh","IJKL","MNOP"]
print(f"Set of words in uppercase are {word_to_upper(string)}")