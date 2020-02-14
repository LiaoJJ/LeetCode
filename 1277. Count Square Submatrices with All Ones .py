'''
naive O(n^3)
1. counting the prefix Sum O(n^2)
2. for each point, count the number of Squares O(n^3)

better O(n^2)
1. define dp[i][j] be the maximum squares using (i,j) as right-bottom point
2. observe that for dp[i][j] to be 3, dp[i-1][j], dp[i][j-1], dp[i-1][j-1] all have to be 2, so we can derive that
    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
'''

class Solution:
    def countSquares(self, A):
        if not A or len(A)==0: return 0
        m, n = len(A), len(A[0])
        res = 0
        for i in range(0, m):
            for j in range(0, n):
                if i==0 or j==0: 
                    res += A[i][j]
                    continue
                if A[i][j]==1:
                    A[i][j] = 1 + min(A[i-1][j], A[i][j-1], A[i-1][j-1])
                    res += A[i][j]
        return res
        