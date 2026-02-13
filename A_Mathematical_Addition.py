t=int(input())
for i in range(t):
    u,v=map(int,input().split())
    if u==1 and v==1:
        print(-1,1)
    else:
        print(1-u,v-1) 