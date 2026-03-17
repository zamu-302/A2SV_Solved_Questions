from collections import deque
n,k=map(int,input().split())
arr=list(map(int,input().split()))
max_=deque()
min_=deque()
ans=0
left=0
count=0
for i in range(len(arr)):
    while max_ and arr[max_[-1]]<arr[i]:
        max_.pop()
    while min_ and arr[min_[-1]]>arr[i]:
        min_.pop()
    min_.append(i)
    max_.append(i)

    while abs(arr[max_[0]]-arr[min_[0]])>k:
        left+=1
        if max_[0]<left:
            max_.popleft()
        if min_[0]<left:
            min_.popleft()
    count+=1
print(2**5 - (left+len(arr)))



