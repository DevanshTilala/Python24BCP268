def remove_empty_tuples(lst):
    return [i for i in lst if i]

lst=[(1,2,3),(),(4,5,6),(),(7,8,9)]
print(f"Before modifications: {lst}")
print(f"After modifications: {remove_empty_tuples(lst)}")