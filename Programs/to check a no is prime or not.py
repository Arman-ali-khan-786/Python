n=int(input("enter a no"))
f=0
i=2
while i<n:
   if n%i==0:
      f=1
      break
   i=i+1
if f==0:
    print("it is a prime no")
else:
    print("it is not a prime no.")
   
