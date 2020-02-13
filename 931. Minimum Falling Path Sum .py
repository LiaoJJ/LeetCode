class Solution:
    def minFallingPathSum(self, A):
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        dp[n-1] = A[n-1][:]
        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = A[i][j] + min(
                    dp[i+1][j-1] if j-1>=0 else float('inf'),
                    dp[i+1][j],
                    dp[i+1][j+1] if j+1<n else float('inf')
                )
        return min(dp[0])