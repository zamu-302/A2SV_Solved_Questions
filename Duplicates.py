from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        num_count=Counter(nums)
        for n in num_count:
            if num_count[n]>1:
                res.append(n)
        return res