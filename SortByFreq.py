from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        t=Counter(s)
        ans=""
        for key,val in sorted(t.items(), key=lambda x: (-x[1], x[0])):
            curr= key*val
            ans+=curr
        return ans
    

        