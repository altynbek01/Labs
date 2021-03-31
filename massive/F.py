n = int(input())
arr = list(map(int, input().split()))
count=0
d=1


while(d!=len(arr)-1):
    if arr[d]>arr[d+1] and arr[d]>arr[d-1]:
        count+=1
    d+=1
print(count)