n=int(input())
q_r,q_c=map(int,input().split())
k_r,k_c=map(int,input().split())
target_r,target_c=map(int,input().split())
if k_r>q_r and k_c<q_c:
    if target_c<q_c and target_r>q_r:
        print("YES")
    else:
        print("NO")
elif k_r>q_r and k_c>q_c:
    if target_c>q_c and target_r>q_r:
        print("YES")
    else:
        print("NO")
elif k_r<q_r and k_c>q_c:
    if target_c>q_c and target_r<q_r:
        print("YES")
    else:
        print("NO")
elif k_r<q_r and k_c<q_c:
    if target_c<q_c and target_r<q_r:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
