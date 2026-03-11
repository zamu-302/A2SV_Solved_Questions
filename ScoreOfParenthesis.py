class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stk=[0]
        for i in range(len(s)):
            if s[i]=="(":
                stk.append(0)
            else:
                last=stk.pop()
                curr=max(last*2,1)

                stk[-1]+=curr
        return stk.pop()