t=int(input())
for _ in range(t):
    n=int(input())

    arr1=list(map(int,input().split()))
    m=int(input())

    arr2=list(map(int,input().split()))

    curr=0
    best=0
    for i in range(n):
        curr+=arr1[i]
        best=max(best,curr)
    
    curr=0
    best2=0
    for i in range(m):
        curr+=arr2[i]
        best2=max(best2,curr)
    print(best+best2)
   