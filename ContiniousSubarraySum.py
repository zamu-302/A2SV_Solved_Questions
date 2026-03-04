class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen={0:-1}
        num=0
        for i in range(len(nums)):
            num+=nums[i]
            num%=k
            if  num not in seen:
                seen[num]=i
            elif i-seen[num]>=2:
                return True
            
        return False
            
            
            