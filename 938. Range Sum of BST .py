# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def help(node):
            if not node: return
            if L<=node.val<=R: self.res += node.val
            if L < node.val:
                help(node.left)
            if node.val < R:
                help(node,right)
        if not root: return 0
        self.res = 0
        help(root)
        return self.res