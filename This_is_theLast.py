t=int(input())
for i in range(t):
    n,coin=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    total=0
    arr.sort(key=lambda x:(x[0],x[1]))
    for i in range(len(arr)):
        if coin<arr[i][0] or coin>arr[i][1]:
            continue
        else:
            coin=max(coin,arr[i][2])
    print(coin)