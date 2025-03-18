def replace_negatives(list1, i=0):
    if i==len(list1):
        return list1
    elif list1[i]<0:
        list1[i]=0
        return replace_negatives(list1, i+1)
    else:
        return replace_negatives(list1, i+1)


print(f"Updated list is: {replace_negatives([-2,-1,-3,0,1,2,3,4,5])}")