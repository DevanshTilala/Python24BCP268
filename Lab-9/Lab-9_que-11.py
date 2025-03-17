def create_list(lst1,lst2):
    return list(set(lst1) & set(lst2))

list1=[1,2,3,4,5]
list2=[2,3,6,8,9]
print(f"Intersection of both the list is: {create_list(list1,list2)}")