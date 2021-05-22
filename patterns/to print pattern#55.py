for a in range(5,0,-1):
    for b in range(5,a,-1):
        print(" ",end="")
    for c in range(6-a,6):
        print(c,end="")
    for d in range(6,a+5):
        print(d,end="")
    print()
