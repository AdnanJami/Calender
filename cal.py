print("Su Mo Tu We Th Fr Sa")
d = 0-2
for i in range(5):

    for j in range(7):
        if d<0:
            print("  ", end=' ')
        elif d<=30:
            if float(d/9)<1:
                print(d + 1, end='  ')
            else:
                print(d + 1, end=' ')
        else:
            print("  ", end=' ')
        d += 1
    print()
