from collections import Counter
t=int(input())
for i in range(t):
    n,l,r=map(int,input().split())
    if l!=0 or r!=0:
        cost=abs((n//2)-l)
        arr=list(map(int,input().split()))
        left=arr[:n//2]
        right=arr[n//2:]
        count=Counter(right)
        for num in left:
            if count[num]>0:
                count[num]-=1
                continue
            else:
                cost+=1
        print(cost)
    else:
        if len(Counter(arr))==
    
