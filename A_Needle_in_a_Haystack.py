from collections import Counter
t=int(input())
for i in range(t):
    s=input()
    t=input()
    ans=""
    seen=Counter(t)
    flag=True
    for i in s:
        if seen[i]==0:
            flag=False
        else:
            seen[i]-=1
    j=0
    res=[]
    for i in sorted(seen):
        res.append(i*seen[i])
    res="".join(res)
    i=0
    j=0
    while i<len(res) or j<len(s):
        if i<len(res):
            if j>=len(s) or res[i]<s[j]:
                ans+=res[i]
                i+=1
            else:
                ans+=s[j]
                j+=1
        else:
            ans+=s[j]
            j+=1
            
    print(ans if flag else "Impossible")
        

