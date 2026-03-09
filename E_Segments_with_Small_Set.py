n,k=map(int,input().split())
arr=list(map(int,input().split()))

left=0
seen=set(arr[0])
count=n+1 if n!=1 else 1
for i in range(1,len(arr)):
    if arr[i] not in seen or i-left+1<=k:
        
        count+=2
        
    else:
        while arr[i] in seen :
            seen.discard(arr[left])
            left+=1
        if i-left+1>k:
            left+=1
            count+=2
print(count)


