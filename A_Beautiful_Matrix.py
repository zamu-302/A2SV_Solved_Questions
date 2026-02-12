t = [list(map(int,input().split())) for _ in range(5)]
for i in range(len(t)):
    if 1 in t[i]:
        for j in range(len(t[i])):
            if t[i][j]==1:
                print(abs(i-2)+abs(j-2))
                break
        break
        

        