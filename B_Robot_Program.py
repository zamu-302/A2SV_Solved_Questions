t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    val=input()
    total=0
    count=0
    for char in val:
        if char=="L":
            total+=1
            x-=1
            if x==0:
                count+=1
                break
        else:
            total+=1
            x+=1
            if x==0:
                count+=1
                break
        
    if count==0:
        print(0)
        continue
    k-=total
    supa=0
    summation=0
    for char in val:
        if char=="L":
            summation+=1
            supa+=1
            if supa==0:
                break
        else:
            summation+=1
            supa-=1
            if supa==0:
                break
    if supa==0:
        print(count +k//summation )
        continue
    else:
        print(1) 

    
    
    

            
