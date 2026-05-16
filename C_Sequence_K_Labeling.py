n,k=map(int,input().split())
arr=list(map(int,input().split()))
count={}
flag=True
for num in arr:
    count[num]=count.get(num,0)+1
    if count[num]>k:
        print("NO")
        quit()
    

if n<k:
    print("NO")
    quit()
else:
    index=[]
    for i in range(n):
        index.append([arr[i],i])
    index.sort()
    res=[0]*n
    curr=1
    for i in range(n):
        res[index[i][1]]=curr
        curr+=1
        if curr>k:
            curr=1
    
    print("YES")
    print(*res)
   
