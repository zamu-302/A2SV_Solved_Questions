from collections import Counter
t=int(input())
for i in range(t):
    n,l,r=map(int,input().split())
    
    arr=list(map(int,input().split()))
    left=arr[:l]
    right=arr[l:]
    left.sort()
    right.sort()

    print(left,right)

       