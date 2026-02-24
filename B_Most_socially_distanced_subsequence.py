t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    left=0
    curr=0
    seen=[]
    for right in range(1,len(arr)):
        if arr[left]>arr[right]:
            seen.append(arr[left])
            seen.append(arr[right])
            left=right

        else:
            if right+1<len(arr) and arr[right]>arr[right+1]:
                seen.append(arr[right])
            else:
                continue
    print(len(seen))
    print(*seen)




