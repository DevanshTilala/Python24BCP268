def modifying_tuple(tup, index, num):
    tup=list(tup)
    tup[index]=num
    return tuple(tup)

tup=(1,2,3,4,5,6,7,8,9)
# print(tup)
# tup=list(tup)
# n1=int(input("Enter the number you want to replace: "))
i=int(input("Enter the index at which you want to replace number: "))
n=int(input("Enter the number you want to replace with: "))

print(modifying_tuple(tup, i, n))
# for i in range(0,len(tup)):
#     if tup[i]==n1:
#         tup[i]=n2
# tup=tuple(tup)
# print(tup)

# lst=[(1,2,3),(4,5,6),(7,8),(9,10,11)]
# print(lst)
# for i in lst:
#     for j in i:
#         if j==6:
#             y=list(i)
#             y[2]=13
#             y=tuple(y)
#             lst.insert(i,y)
# print(lst)
