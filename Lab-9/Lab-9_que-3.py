def createArray(r1,r2,r3,n):
    lst=[[[n for i in range(r1)] for j in range(r2)] for k in range(r3)]
    return lst

print(createArray(3,4,5,4))
