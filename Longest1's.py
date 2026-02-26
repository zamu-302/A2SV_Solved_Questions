class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        left=0
        ans=0
        seen=Counter()
        max_freq=0
        res=0
        for right in range(len(nums)):
            seen[nums[right]]+=1
            while seen[0]>1:
                seen[nums[left]]-=1
                left+=1
            res=max(res,seen[1])
        return res
            
                

                
            
            
            
        
            


        
        