'''
very hard for me
dp[i][j]== dp[i-1][j-1] + 1 if s[i]==s[j]
            max(dp[i-1][j], dp[i][j-1]) else
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
'''


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(m-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]