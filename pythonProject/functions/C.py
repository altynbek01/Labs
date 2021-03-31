def xor( x,y):
    if(x==1 & y==1):
     return  (0)
    elif(x==0 & y==0):
        return (0)
    elif (x==0 & y==1) :
        return (1)
    elif ((x==1 & y==0)):
        return  1


print(xor(int(input()), int(input())))