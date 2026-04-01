# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        #idea is that we take the max of the nums and rather than taking the number we take the index
        # and we will recusively divide the the nums to left and right
        
        def find_max(nums):
            curr=-1
            idx=0
            for i in range(len(nums)):
                if nums[i]>curr:
                    idx=i
                    curr=nums[i]
            return idx
        def dfs(arr):
            if not arr:
                return 


            
            
            

            idx=find_max(arr)
            root=TreeNode(arr[idx])
            left=arr[:idx]
            right=arr[idx+1:]
            root.left=dfs(left)
            root.right=dfs(right)
            return root
        return dfs(nums)







        





        