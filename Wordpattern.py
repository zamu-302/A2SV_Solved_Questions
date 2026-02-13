from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split()
        if len(set(pattern))!=len(set(s)) or len(s)!=len(pattern):
            return False
        ans=Counter()
        for a,b in zip(pattern,s):
            curr=(a,b)
            ans[curr]+=1
        return len(ans.keys())==len(set(s))
