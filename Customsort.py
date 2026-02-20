from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=Counter(s)
        res=""
        for i in range(len(order)):
            if count[order[i]]>0:
                res+=order[i]*count[order[i]]
        for i in sorted(s):
            if i not in order:
                res+=i
        return res
            


        