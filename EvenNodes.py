# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans=0
        def preorder(node,father,grand):
            nonlocal ans
            if not node:
                return
            
            if grand%2==0:
                ans+=node.val
            
            temp=father
            father=node.val
            grand=temp

           
            preorder(node.left,father,grand) 
            preorder(node.right,father,grand) 
            
        preorder(root,1,1)
        return ans
       

        