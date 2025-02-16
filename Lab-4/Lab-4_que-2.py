def multiplication_table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

n=int(input("Enter a number: "))
print("Multiplication table is: ")
multiplication_table(n)