'''
this is really a hard one for me
https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1%2Bdpn-3
'''

class Solution:
    def numTilings(self, N: int) -> int:
        MOD = int(1e9)+7
        dp = [0]*max(N+1, 4)
        dp[1], dp[2], dp[3] = 1, 2, 5
        if N<=3: return dp[N]
        for i in range(4, N+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
            dp[i] %= MOD
        return dp[i]