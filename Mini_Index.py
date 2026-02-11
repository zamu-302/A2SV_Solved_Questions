from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        left=Counter()
        n=len(nums)-1
        for i in range(len(nums)):
            left[nums[i]]+=1
            count[nums[i]]-=1
            if left[nums[i]]*2>i+1 and count[nums[i]]*2>n-i:
                return i
        return -1


        