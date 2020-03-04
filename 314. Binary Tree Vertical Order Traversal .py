'''
since it requires output from left to right, from up to bottom.
using level order traverse, a.k.a BFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        c = collections.defaultdict(list)
        res = []
        queue = collections.deque()
        queue.append([root, 0])
        while queue:
            u, loc = queue.popleft()
            c[loc].append(u.val)
            if u.left: queue.append([u.left, loc-1])
            if u.right: queue.append([u.right, loc+1])
        for i in sorted(c.keys()):
            res.append(c[i])
        return res