class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        
        nums.sort()
        cnt=1
        curr=1
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                curr+=1
                cnt=max(curr,cnt)
                continue
            if nums[i]==nums[i-1]:
                continue
            
            curr=1
            
        
        return cnt
            
