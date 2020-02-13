'''

1. DP: I don't learn this solution, too hard for me.

2. Stack O(n^2)

'''

class Solution:
    def maximalRectangle(self, A):
        def findLargestRectangle(height):
            # print(height, n)
            stack = [-1]
            for i in range(n+1):
                while height[i]<height[stack[-1]]:      # be careful, this one must be while, not if!!!
                    h = height[stack.pop()]
                    w = i-stack[-1]-1
                    self.res = max(self.res, w*h)
                stack.append(i)

        if not A or len(A)==0 or len(A[0])==0: return 0
        m, n = len(A), len(A[0])
        height = [0]*(n+1)
        self.res = 0
        for i in range(m):
            for j in range(n):
                height[j] = (height[j]+1 if A[i][j]=="1" else 0)
            findLargestRectangle(height)
        return self.res