for a in range(5,0,-1):
    for b in range(5,a,-1):
        print(" ",end="")
    for c in range(a,0,-1):
        print(c,end="")
    for d in range(2,a+1):
        print(d,end="")
    print()
