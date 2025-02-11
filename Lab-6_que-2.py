details=[("S1",1,18),("S2",2,17),("S3",3,16)]
roll_num=[]
age=[]
name=[]

for i in details:
    if isinstance(i,tuple):
        name.append(i[0])
        roll_num.append(i[1])
        age.append(i[2])

print(f"List of names: {name}\nRoll numbers: {roll_num}\nList of age is: {age}")