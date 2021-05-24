n=int(input("enter a no"))
s=0
b=n
while n>0:
    d=n%10
    s=(s*10)+d
    n=n//10
a=s
if b==a:
    print(b,"is a palindrom no.")
else:
    print(b,"is not a palindron no.")
