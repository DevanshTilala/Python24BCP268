a=input("Enter a string: ")
count=0

for i in a:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or
       i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
       count+=1

print("There are",count,"vowels in",a)