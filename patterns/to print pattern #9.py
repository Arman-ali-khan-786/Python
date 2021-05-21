for a in range(1,6):
    for b in range(1,6):
        if a==b or a+b==6:
            print("1",end="")
        else:
            print("0",end="")
    print()
