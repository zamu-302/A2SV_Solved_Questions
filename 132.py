class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk=[]
        m=-float("inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<m:
                return True
            while stk and stk[-1]<nums[i]:
                m=stk.pop()
            stk.append(nums[i])
        return False
