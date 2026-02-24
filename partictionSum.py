class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen={}
        for i in range(len(s)):
            seen[s[i]]=i
        left=0
        right=-1
        res=[]
        for i in range(len(s)):
            right=max(right,seen[s[i]])
            if right==i:
                res.append(i-left)
                left=i
        res[0]+=1
        return res
