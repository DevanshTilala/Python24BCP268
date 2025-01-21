def remove(mainstring, removestring):
    newstring=""
    for i in mainstring:
        if i not in removestring:
            newstring+=i
    return newstring

print(remove("abcdef","cd"))