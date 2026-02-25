t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    maxi=max(arr)
    for i in range(1,len(arr)):
        if i==0:
            if arr[i]<arr[i+1]:
                continue
            else:
                arr[i+1]=max(arr[:i+1])
        else:
            if i+1<len(arr)and  arr[i]<=arr[i+1] and (i+1)%2==0:
                if arr[i]==arr[i+1]:
                    count+=1
                else:
                    count+=arr[i+1]-arr[i]
            elif i+1<len(arr) and arr[i]>arr[i+1] and (i+1)%2==1:
                arr[i+1]=10**9
            
    print(count)


