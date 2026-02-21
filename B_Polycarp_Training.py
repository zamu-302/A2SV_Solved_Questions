t=int(input())
arr=list(map(int,input().split()))
arr.sort()
j=0
for i in range(t):
    if j>=arr[i]:
        continue
    j+=1
print(j)