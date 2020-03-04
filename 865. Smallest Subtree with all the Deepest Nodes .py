# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def help(node):
            if not node: return None, 0

            left, depthL = help(node.left)
            right,depthR = help(node.right)
            if depthL < depthR:
                return right, depthR + 1
            elif depthL > depthR:
                return left, depthL + 1
            else:
                return node, depthL
        if not root: return None
        return help(root)[0]