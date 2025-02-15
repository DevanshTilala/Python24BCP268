def sort_by_price(food_list):
    return sorted(food_list, key=lambda x:x[1], reverse=True)

food_details=[("F1",20),("F2",50),("F3",10),("F4",100)]

print(f"Sorted food details are {sort_by_price(food_details)}")
# food_details.sort(key=lambda x:x[1],reverse=True)
# print(food_details)