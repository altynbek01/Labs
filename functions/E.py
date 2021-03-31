x=int(input())
y=1
count=0
while(y<=x):
    if(x%y==0):
        count+=1
    y+=1
if count==2:
    print('prime')
elif count>2 :
    print('composite')
elif  count==1:
    print('composite')