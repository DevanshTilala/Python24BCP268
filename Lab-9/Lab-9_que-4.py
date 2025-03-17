def sum_avg(sub1,sub2,sub3,sub4,sub5):
    total=sub1+sub2+sub3+sub4+sub5
    average=total/5

    return total,average

Maths=int(input("Enter the marks of Maths: "))
Phy=int(input("Enter the marks of Physics: "))
Chem=int(input("Enter the marks of Chemistry: "))
PCo=int(input("Enter the marks of English: "))
Comp=int(input("Enter the marks of Computer: "))
total,average=sum_avg(Maths,Phy,Chem,PCo,Comp)
print(f"Your total is: {total}\nYour average is: {average}")