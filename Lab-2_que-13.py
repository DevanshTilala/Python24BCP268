words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen",
         "sixteen","seventeen","eighteen","nineteen"]

a=int(input("Enter a number[0-19]: "))

if 0<=a<=19:
    print(f"{a} -> {words[a]}")
else:
    print("Please enter valid number")