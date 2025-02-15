def modifying_tuple(tup, index, num):
    tup=list(tup)
    tup[index]=num
    return tuple(tup)

tup=(1,2,3,4,5,6,7,8,9)
print(f"Tuple is {tup}")
# print(tup)
# tup=list(tup)
# n1=int(input("Enter the number you want to replace: "))
try:
    i=int(input("Enter the index at which you want to replace number: "))
    n=int(input("Enter the number you want to replace with: "))
except ValueError:
    print("\n\t\t!!! Please enter the valid number !!!")
    

try:
    print(f"Modified tuple is {modifying_tuple(tup, i, n)}")
except IndexError:
    print("\n\t\t!!! Index out of range. Please enter the valid value for index !!!")
except ValueError and NameError:
    print("\n\t\t!!! Please enter the valid number !!!")
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
