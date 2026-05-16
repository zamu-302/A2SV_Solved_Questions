t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    if arr==sorted(arr):
        print('YES')
    elif x==n:
        print("NO")
    else:
        