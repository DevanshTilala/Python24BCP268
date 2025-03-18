def power(a,b):
    if b==0:
        return 1
    return a * power(a,b-1)

num=float(input("Enter a number: "))
raiseto=int(input("Enter the power to which you want to find the value: "))
print(f"Value of given number is {power(num,raiseto)}")