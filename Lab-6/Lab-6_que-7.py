def del_element_tuple(tup, num):
    tup=list(tup)
    if num in tup:
        tup.remove(num)

    return tuple(tup)

tup=(1,2,3,4,5,6,7,8,9)
print(tup)
n=int(input("Enter the number you want to remove: "))

print(del_element_tuple(tup,n))