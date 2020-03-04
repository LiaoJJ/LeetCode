'''
BF C(n,k)*n  O(n!)

LeetCode 516
DP find the longest palindrome sequence O(n^2)

'''


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(str)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-2, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]+k >=len(s)