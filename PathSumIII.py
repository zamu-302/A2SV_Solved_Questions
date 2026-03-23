from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:

        seen=defaultdict(int)
        seen[0]=1
        def dfs(node,total):
            count=0
            if  node:
                total+=node.val
                count=seen[total-target]

                seen[total]+=1
                count+=dfs(node.left,total)+dfs(node.right,total)
                seen[total]-=1
            return count
        return dfs(root,0)


               
            
           