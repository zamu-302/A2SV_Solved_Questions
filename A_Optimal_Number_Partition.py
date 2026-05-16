t=int(input())
arr=list(map(int,input().split()))

arr.sort()
left=0
right=len(arr)-1
ans=0
while left<right:
    ans+=((arr[left]+arr[right])**2)
    left+=1
    right-=1
print(ans)
