def rev_list(list1, x):
    if x==0:
        return list1
    return rev_list(list1[:])

print(rev_list([1,2,3,4,5],len([1,2,3,4,5])-1))