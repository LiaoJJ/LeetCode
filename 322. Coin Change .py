'''
coin cahnge, similar to LC 279
1. DP O(nk)
2. BFS O(k^(n/max)) (I guess)
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        # print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        f1 = [amount]
        level = 0
        visited = set()
        while f1:
            f2 = []
            for cur in f1:
                if cur==0: return level
                if cur in visited: continue
                visited.add(cur)
                for c in coins:
                    if c<=cur:
                        f2.append(cur - c)
            level += 1
            f1 = f2
        return -1