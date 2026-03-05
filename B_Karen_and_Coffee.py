n,m,k=map(int,input().split())
arr=[]
for i in range(n):
   
    arr.append(list(map(int, input().split())))
curr=0
for i in range(len(arr)):
    curr=max(curr,arr[i][1])

event=[0]*200002
for a,b in arr:
    event[a]+=1
    event[b+1]-=1
for i in range(1,len(event)):
    event[i]+=event[i-1]

for i in range(1,len(event)):
    event[i]= 1 if event[i]>=m else 0
for i in range(1,len(event)):
    event[i]+=event[i-1]
for i in range(k):
    a,b=map(int,input().split())
    print(event[b]-event[a-1])




