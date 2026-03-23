# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if p and q:
                return p.val==q.val and isSame(p.left,q.left) and isSame(p.right,q.right)
            return p is q
            
        def dfs(node):
            if not node:
                return False
            
            if isSame(node,subRoot):
                return True

            left=dfs(node.left)
            right=dfs(node.right)
            return left or right
        return dfs(root)
    

            

        