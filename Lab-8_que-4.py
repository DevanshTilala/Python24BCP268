import string
def separate_names(name):
    names_A=set()
    names_B=set()

    for i in name:
        if i[0].startswith("A") or i[0].startswith("a"):
            names_A.add(i)
        else:
            names_B.add(i)
    
    return names_A,names_B

names={"AAA","BBB","ABB","BAA","ABA","BAB"}
print(separate_names(names))