from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        a=Counter(changed)
        zero,m=divmod(a[0],2)
        if m: return []
        res=[0]*zero
        for i in sorted(a.keys()):
            if a[i]>a[2*i]:
                return []
            a[2*i]-=a[i]
            res.extend([i]*a[i])
        
        return res
