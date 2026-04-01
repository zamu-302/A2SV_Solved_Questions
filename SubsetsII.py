class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def dfs(index,arr):
            ans.append(arr[:])
            
            



            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                arr.append(nums[i])
                dfs(i+1,arr)
                arr.pop()
        dfs(0,[])
        return ans

        