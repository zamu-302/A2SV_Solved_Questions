class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for i in range(len(s)):
            if s[i] != "*":
                stk.append(s[i])
                continue
        
            elif stk:
                    stk.pop()
        return "".join(stk)
            
                
