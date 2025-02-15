def del_element_tuple(tup, num):
    tup=list(tup)
    if num in tup:
        tup.remove(num)
    else:
        return 0

    return tuple(tup)

tup=(1,2,3,4,5,6,7,8,9)
print(tup)
n=int(input("Enter the number you want to remove: "))

if(del_element_tuple(tup,n)):
    print(f"Modified tuple is {del_element_tuple(tup,n)}")
else:
    print("Element not in tuple")
