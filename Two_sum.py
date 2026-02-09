class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            compilement=target-nums[i]
            if compilement in seen:
                return [i,seen[compilement]]
            seen[nums[i]]=i


        