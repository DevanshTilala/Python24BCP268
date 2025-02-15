name_list=[("B1","B2","B3"),"G1","G2","G3"]
countg,countb=0,0

for i in name_list:
    if isinstance(i,tuple):
        countb=len(i)
    else:
        countg+=1

print(f"Number of girls is {countg}\nNumber of boys is {countb}")