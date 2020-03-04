# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root: return -1
        cur = root
        res = root.val
        dif = float('inf')
        while cur:
            if abs(cur.val - target) < dif:
                dif = abs(cur.val - target)
                res = cur.val
            if cur.val <= target:
                cur = cur.right
            else:
                cur = cur.left
        return res