from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_num=Counter(nums)
        for num in count_num:
            if count_num[num]==1:
                return num
        