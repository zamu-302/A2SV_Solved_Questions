class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq=0
        seen={}
        res=0
        left=0
        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1
            max_freq=max(max_freq,seen[s[right]])
            while (right-left+1)-max_freq>k:
                seen[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
        
        