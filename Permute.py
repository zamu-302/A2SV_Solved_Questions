class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        #[1,2,3]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            x=self.permute(nums)#[[3]]
            for perm in x:
                perm.append(n)
            res.extend(x)
            nums.append(n)
        return res
    

        