# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
        
            if not node.left and not node.right:
                return 1
            elif not node.left:
                return 1+depth(node.right)
            elif not node.right:
                return 1+depth(node.left)
            else:
                return min(1+depth(node.left),1+depth(node.right))
        return depth(root) if root else 0

            
        



        