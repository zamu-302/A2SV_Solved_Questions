t=int(input())
for i in range(t):
    n=int(input())
    enem=list(input())
    play=list(input())
    ans=0
    for i in range(n):
            if play[i] == '1':
                if i > 0 and enem[i-1] == '1':
                    ans += 1
                    enem[i-1] = '2' 
                elif enem[i] == '0':
                    ans += 1
                    enem[i] = '2' 
                elif i < n - 1 and enem[i+1] == '1':
                    ans += 1
                    enem[i+1] = '2'
    print(ans)
            

