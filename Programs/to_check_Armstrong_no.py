n=int(input("enter a no: "))
s=0
a=n
while a>0:
    d=a%10
    s=s+(d**3)
    a=a//10
if n==s:
    print("it is an armstrong no")
else:
    print("it is not an armstrong no")
