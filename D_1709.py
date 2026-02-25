t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    seen={}
    res=[]
    for i in range(len(a)):
        swapped=False
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                res.append([1,j+1])
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break
    for i in range(len(b)):
        swapped=False
        for j in range(0,len(b)-i-1):
            if b[j]>b[j+1]:
                res.append([2,j+1])
                b[j],b[j+1]=b[j+1],b[j]
                swapped=True
        if not swapped:
            break
    
    for i in range(len(a)):
        if a[i]>b[i]:
            res.append([3,i+1])
            a[i],b[i]=b[i],a[i]
    print(len(res))
    if len(res)>0:
        for num in res:
            print(*num)
    


    
    

  



