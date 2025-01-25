def prime(num):

    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

def perfect_num(num):
    sum=0
    for i in range(1,num+1):
        if(num%i==0):
            sum+=i
    
    if(sum==(num*2)):
        return True
    else:
        return False

def armstrong_num(num):
    sum=0
    a=num
    while num!=0:
        sum+=(num%10)**3
        num//=10

    if a==sum:
        return True
    else:
        return False

def palindrome(num):
    sum=0
    while num!=0:
        sum+=num%10
        sum*=10
        num//=10
    
    sum//=10
    return sum

def automorphic(num):
    num1=num**2
    
    while num>0:
        if (num%10 != num1%10):
            return False
    
        num//=10
        num1//=10

    return True

n=int(input("Enter a number: "))

if prime(n):
    print("It is a prime number")
if perfect_num(n):
    print("It is a perfect number")
if armstrong_num(n):
    print("It is an armstrong number")
if palindrome(n)==n:
    print("It is a palindrome")
if automorphic(n):
    print("It is automorphic number")