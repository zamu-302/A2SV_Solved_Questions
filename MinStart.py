class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr=0
        now=0
        for i in range(len(nums)):
            now+=nums[i]
            curr=min(curr,now)
        return 1 if curr==0 else abs(curr)+1
        