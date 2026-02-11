from collections import Counter
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        res=[]
        for a,b in zip(s1,s2):
            if a!=b:
             res.append(f"{a}{b}")
        count=Counter(res)
        xy = count["xy"]
        yx = count["yx"]
        ans = xy // 2 + yx // 2
        xy %= 2
        yx %= 2
        if xy == 1 and yx == 1:
            ans += 2
        elif xy != 0 or yx != 0:
            return -1

        return ans