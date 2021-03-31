n = int(input())
arr = (map(int, input().split()))
arr2=list(arr)

arr2.sort()

max=arr2[len(arr2)-1]
while(max==arr2[len(arr2)-1]):
    arr2.pop()
secondMax=arr2[len(arr2)-1]
print(secondMax)
