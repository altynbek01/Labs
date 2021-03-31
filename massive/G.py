n = int(input())
arr = list(map(int, input().split()))
arr2=[]
count=0
d=len(arr)-1


while(d!=-1):
    arr2.append(arr[d])
    d-=1
print(arr2)
