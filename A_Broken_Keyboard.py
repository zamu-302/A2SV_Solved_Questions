t=int(input())
for i in range(t):
    s=input()
    s = s + '*'
    left=0
    res=[]
    if len(s)!=1:
        for right in range(len(s)):
            if right+1<len(s) and s[right]==s[right+1]:
                continue
            elif right+1<len(s) and s[right]!=s[right+1]:
                if s[right] not in res and (right-left+1)%2!=0:
                    res.append(s[right])
                left=right+1
                continue
            
                
        res.sort()
        print("".join(res))
    else:
        print(s[0])
        
    

    
   
                