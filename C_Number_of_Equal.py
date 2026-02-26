from collections import Counter
n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
left=Counter(arr2)
count=0
for num in arr1:
    count+=left[num]
print(count)


