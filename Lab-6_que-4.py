food_details=[("F1",20),("F2",50),("F3",10),("F4",100)]

food_details.sort(key=lambda x:x[1],reverse=True)
print(food_details)