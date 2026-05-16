import math
t=int(input())
for i in range(t):
    num="3141592653589793238462643383279"
    left=0
    arr=input()
    count=0
    if arr[0]==num[0]:
        while left<len(arr):
            if num[left]==arr[left]:
                count+=1
                left+=1
            else:
                break
        
           
    print(count)
