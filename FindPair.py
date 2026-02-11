from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        letter=Counter(s)
        ans=""
        for i in range(1,len(s)):
            if letter[s[i-1]]==int(s[i-1]):
                ans+=s[i-1]
                if letter[s[i]]==int(s[i]) and s[i]!=s[i-1]:
                    ans+=s[i]
                    return ans
                ans=""
            ans=""
        return ans


        