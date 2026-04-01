class Solution:
    def wordBreak(self, s: str, seen: List[str]) -> List[str]:
        res=[]
        ans=""
        def dfs(i,arr):
            if i==len(s):
                res.append(arr[:-1])
            
                




            for j in range(i,len(s)):

                if s[i:j+1] in seen:
                    dfs(j+1,arr+s[i:j+1]+" ")
                
        dfs(0,"")
        return res
               
            
                    

        