from collections import Counter
n,k=map(int,input().split())

arr1=list(map(int,input().split()))
target=k-len(set(arr1))
arr2=list(map(int,input().split()))
count=Counter(arr1)
idx=[i for i in range(len(arr1))]
idx.sort(key=lambda x:arr2[x])

ans=0
for num in idx:
    if count[arr1[num]]>1 and target>0:
       
        ans+=arr2[num]
        target-=1
        count[arr1[num]]-=1
print(ans)