
'''
knapsack problem
dp[i][j] means the total number of combinations to reach j by number of i coins
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins)+1, (amount+1)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i-1]] if j-coins[i-1]>=0 else 0) 
        return dp[m-1][n-1]

'''
space optimization
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins)+1, (amount+1)
        dp = [0]*n
        dp[0] = 1
        for coin in coins:
            for j in range(coin, n):
                dp[j] += dp[j-coin]
        return dp[n-1]