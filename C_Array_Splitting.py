n,k=map(int,input().split())
arr=list(map(int,input().split()))
total=0
trials=[]
curr_max=arr[-1]-arr[0]
for i in range(len(arr)-1,-1,-1):
    trials.append(arr[i]-arr[i-1])
trials.sort(reverse=True)
for i in range(k-1):
    curr_max-=trials[i]

print(curr_max)



