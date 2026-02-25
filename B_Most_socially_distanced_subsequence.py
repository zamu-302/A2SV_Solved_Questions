t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    left=0
    curr=0
    seen=[arr[0]]
    for i in range(1,len(arr)):
        if i+1<len(arr) and arr[i-1]>arr[i]<arr[i+1]:
            seen.append(arr[i])
        elif i+1<len(arr)and arr[i-1]<arr[i]>arr[i+1]:
            seen.append(arr[i])
        elif i+1==len(arr):
            seen.append(arr[i])
        else:
            continue
    print(len(seen))
    print(*seen)
         
    
   



