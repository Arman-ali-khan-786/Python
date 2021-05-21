for a in range(9,0,-2):
    for b in range(10,a,-2):
        if a%3==1 or a%3==0:
           print("1",end="")
        else:
            print("0",end="")
    print()
