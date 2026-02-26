x,y=map(int,input().split())
arr=list(map(int,input().split()))
left=0
res=10**9
curr=0
count=0
for right in range(x):
    curr+=arr[right]
    while y<curr:
        res=min(res,right-left+1)
        curr=curr-arr[left]
        left+=1
    count+=right-left+1
    
    
    
    
print(count)
    

    