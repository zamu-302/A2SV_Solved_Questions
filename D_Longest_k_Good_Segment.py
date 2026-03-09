from collections import Counter
n,k=map(int,input().split())
arr=list(map(int,input().split()))
seen=Counter()
ans=[1,k]
max_len=0
left=0
for right in range(len(arr)): 
    
        seen[arr[right]]+=1
        while len(seen)>k:
            seen[arr[left]]-=1
            if seen[arr[left]]==0:
                del seen[arr[left]]
            left+=1

        curr=right-left+1
        if curr>max_len:
            max_len=curr
            ans[0],ans[1]=left+1,right+1
    
           
print(*ans)


   
      


