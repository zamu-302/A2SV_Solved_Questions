t=int(input())
arr=[]
for i in range(t):
    arr.append(list(map(int,input().split())))
idx=[i for i in range(len(arr))]
idx.sort(key=lambda x:(arr[x][0],arr[x][1]))
arr.sort(key=lambda x:(x[0],x[1]))
ans=-1
for i in range(1,len(arr)):
    if (arr[i][0]>arr[i-1][1]):
        break
    else:
        ans=i+1
print(ans)



    