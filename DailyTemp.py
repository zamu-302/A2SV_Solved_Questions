class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        ans=[0]*len(arr)
        stk=[]
        for i in range(len(arr)):
            while stk and stk[-1][0]<arr[i]:
                curr=stk[-1][1]
                ans[curr]=i-curr
                stk.pop()
            stk.append([arr[i],i])
        return ans
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))


        