# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            if left is None:
                return None

            right = dfs(node.right)
            if right is None:
                return None

            if abs(left - right) > 1:
                return None

            return 1 + max(left, right)

        return dfs(root) is not None