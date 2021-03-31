def election( x,y,z):
    a=[]
    a.append(x)
    a.append(y)
    a.append(z)
    zero= a.count(0)
    one=a.count(1)
    if zero>one:
        return 0
    else:
        return 1




print(election(int(input()), int(input()), int(input())))