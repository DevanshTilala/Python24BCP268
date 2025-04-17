# flag=1
# while flag:
#     try:
#         num=int(input("Enter a integer: "))
#     except NameError as e:
#         flag=1
#     except ValueError as e:
#         flag=1
#     else:
#         flag=0

while True:
    try:
        num=int(input("Enter a integer: "))
        break
    except:
        print("Invalid input! Enter a integer")