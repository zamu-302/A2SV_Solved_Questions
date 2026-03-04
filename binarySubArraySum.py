class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        another={0:1}
        curr=0
        ans=0 
        for i in range(len(nums)):
            curr+=(nums[i])
            if curr-goal in another:
                ans+=another[curr-goal]
            another[curr]=another.get(curr,0)+1
        return ans
        
        
        