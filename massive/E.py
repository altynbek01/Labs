n = int(input())
arr = list(map(int, input().split()))
count=0
d=0


while(d!=len(arr)-1):
    if ((arr[d]>0) and (arr[d+1]>0)) or ((arr[d]<0) and (arr[d+1]<0)) or ((arr[d]==0) and (arr[d+1]==0)) :
        count+=1
    d+=1
if count>0:
    print('YES')
else:
    print('NO')