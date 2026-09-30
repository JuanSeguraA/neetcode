# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node, order):
            if node is None:
                order.append(None)
                return
            order.append(node.val)
            dfs(node.left, order)
            dfs(node.right, order)

        order_p, order_q = [], []
        dfs(p, order_p)
        dfs(q, order_q)
        return order_p == order_q