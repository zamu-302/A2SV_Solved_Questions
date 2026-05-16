t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    ans=0
   
   
    turn=1
    for i in range(0,len(arr)-1,2):
        diff=arr[i]-arr[i+1]

        use=min(diff,k)
        k-=use
        ans+=diff-use
    if n%2==1:
        ans+=arr[-1]
    
    print(ans)
