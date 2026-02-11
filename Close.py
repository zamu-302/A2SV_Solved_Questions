from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        a=Counter(word1)
        b=Counter(word2)
        if a==b:
            return True
        for w in word1:
            if w not in word2:
                return False
        value1=list(a.values())
        value2=list(b.values())
        value1.sort()
        value2.sort()
        return value1==value2
            
        