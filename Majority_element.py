from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num=(len(nums)//3)
        res=[]
        count=Counter(nums)
        for k in count:
            if count[k]>num:
                res.append(k)
        return res
        