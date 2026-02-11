from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s=Counter(s)
        t=Counter(t)
        count=0
        for letter in s:
            if s[letter]>t[letter]:
                curr=s[letter]-t[letter]
                count+=curr
        return count
            