class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        seen={}
        for i in range(len(num)):
            if num[i] not in seen:
                seen[num[i]]=i
        res=[]
        for i in range(len(nums)): 
            res.append(seen[nums[i]])
        return res
