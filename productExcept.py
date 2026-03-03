class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeros=0
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeros+=1
        if zeros>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                if zeros>0:
                    nums[i]=0
                else:
                    nums[i]=prod//nums[i]
            else:
                nums[i]=prod
        return nums

        