class Solution:
    def maximalSquare(self, A):
        if not A or len(A)==0: return 0
        m, n = len(A), len(A[0])
        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j]=='1':
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1],
                        dp[i-1][j],
                        dp[i][j-1]
                    )
                res = max(res, dp[i][j])
        return res**2