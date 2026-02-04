class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=max(nums)
        for i in range(a+1):
            if i not in nums:
                return i
        else:
            return a+1
        