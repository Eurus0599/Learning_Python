n= int(input("Enter a Number"))
if (int(n)!=n):
    print("Enter an integer number")
copy= n
s=0
while (copy>0):
    s+= copy%10
    copy=copy//10
if (n%s==0):
    print("It is a Harshad Number")
else:
    print("Not a Harshad Number") 
           
