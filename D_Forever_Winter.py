from collections import defaultdict
from collections import Counter
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    seen=defaultdict(int)

    for j in range(m):
        a,b=list(map(int,input().split()))
        seen[a]+=1
        seen[b]+=1
    
    degree_counts=Counter(seen.values())
    if 1 in degree_counts:
        del degree_counts[1]
    if len(degree_counts)==1:
        x=list(degree_counts.keys())[0]
        y=x-1
    else:
        for deg,count in degree_counts.items():
            if count==1:
                x=deg
            else:
                y=deg-1
    print(x,y)
