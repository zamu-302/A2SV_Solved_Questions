class Solution:
    def splitString(self, s: str) -> bool:
       
        def dfs(index,prev):
            if index==len(s):
                return True

            for i in range(index,len(s)):
                val=int(s[index:i+1])
                if val==prev-1:
                    if dfs(i+1,val):
                        return True
                elif val>=prev:
                    break
            return False
        
        for i in range(len(s)-1):
            first=int(s[:i+1])
            if dfs(i+1,first):
                return True
        return False
                
        



        