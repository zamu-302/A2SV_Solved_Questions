t=int(input())
for i in range(t):
    n=int(input())
    arr=input()
    arr2=input()
    arr+="0"
    arr2+="0"
    count=0
    flag=True
    for i in range(len(arr)-1):
        count+=(arr[i]=='1')-(arr[i]=='0')

        if ((arr[i]==arr2[i])!=(arr[i+1]==arr2[i+1]) and count!=0):
            flag=False
            break
    print("YES" if flag else "NO")
        
        
   
   


          
