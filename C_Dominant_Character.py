t=int(input())
potential=["aca","aa","acba","abca","aba","abbacca", 
    "accabba"]
res=[]
for i in range(t):
    n=int(input())
    trail=input()
    for seq in potential:
        if seq in trail:
            res.append(len(seq))
    print(min(res) if res else -1)
    res=[]