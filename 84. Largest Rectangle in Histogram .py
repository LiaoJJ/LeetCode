'''
classis Stack O(n)
    when it's increasing, then just push to stack
    when it's decreasing, then continue to pop, and calculate the rectangle area, until it's back to increasing
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights)==0: return 0
        stack = [-1]
        heights.append(0)
        n = len(heights)
        res = 0
        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                res = max(res, w*h)
            stack.append(i)
        return res