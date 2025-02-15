def count(name_list):
    boys_count,girls_count=0,0
    for i in name_list: 
        if isinstance(i,tuple):
            boys_count+=len(i)
        else:
            girls_count+=1 
    
    return girls_count, boys_count

name_list=[("B1","B2","B3"),"G1","G2","G3"]
girls,boys=count(name_list)

print(f"Number of girls is {girls}\nNumber of boys is {boys}")