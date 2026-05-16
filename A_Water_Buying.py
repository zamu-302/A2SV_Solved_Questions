t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    cost=0
    if a*2<=b:
        print(n*a)
    else:
        if n%2==1:
           print(b*(n//2)+a)
        else:
            print((n//2)*b)
    
