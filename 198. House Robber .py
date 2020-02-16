class Solution:
    def rob(self, A: List[int]) -> int:
        if not A: return 0
        n = len(A)
        dp = [0]*n
        for i in range(n):
            dp[i] = max(
                dp[i-1] if i-1>=0 else 0, 
                (dp[i-2] if i-2>=0 else 0) + A[i]
            )
        return dp[n-1]