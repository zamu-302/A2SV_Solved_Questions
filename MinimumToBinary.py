class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if len(nums)-i>=3 and nums[i]==0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                count+=1
        if 0 not in nums:
            return count
        return -1
        
        