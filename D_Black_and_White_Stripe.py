t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=input()
    left=0
    count=0
    curr=10**6
    right=0
    while right<(len(arr)):
        if right-left+1<k:
            if arr[right]=='W':
                count+=1      
        else:
            if arr[right]=='W':
                count+=1 
            curr=min(curr,count)
            if arr[left]=="W":
                count-=1
            left+=1
        right+=1
    
            
    print(curr)
            
            


