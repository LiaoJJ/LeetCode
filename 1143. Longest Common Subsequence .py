class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        m, n = len(t1), len(t2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if t1[i]==t2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i-1>=0 and j-1>=0  else 0) + 1
                else:
                    dp[i][j] = max(
                        dp[i-1][j] if i-1 >=0 else 0,
                        dp[i][j-1] if j-1 >=0 else 0,
                    )
        return dp[m-1][n-1]