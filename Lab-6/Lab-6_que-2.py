def sep_details(list):
    names=[i[0] for i in list if isinstance(i,tuple)]
    roll_num=[i[1] for i in list if isinstance(i,tuple)]
    age=[i[2] for i in list if isinstance(i,tuple)]

    return names, roll_num, age

details=[("S1",1,18),("S2",2,17),("S3",3,16)]

name,roll_num,age=sep_details(details)

print(f"List of names: {name}\nRoll numbers: {roll_num}\nList of age is: {age}")