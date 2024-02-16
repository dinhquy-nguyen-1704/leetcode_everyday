# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []
        @cache
        def inorder(x):
            if x is not None:
                inorder(x.left)
                l.append(x.val)
                inorder(x.right)

            return l

        l = inorder(root)
        return l

        
        