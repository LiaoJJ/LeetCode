'''
this is really a classic problem
1. DP O(n*sqrt(n))
you have to use static array, otherwise TLE

2. BFS 
'''

class Solution:
    _dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self._dp
        while len(dp)<=n:
            cur = len(dp)
            temp = float('inf')
            for i in range(1, int(math.sqrt(cur)+1)):
                temp = min(temp, dp[cur - i*i] + 1)
            dp.append(temp)
        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        cand = [i*i for i in range(1, int(n**0.5+1))]
        visited = set()
        level = 0
        f1 = [n]
        while f1:
            f2 = []
            for cur in f1:
                if cur in visited: continue
                visited.add(cur)
                for c in cand:
                    if cur==c: return level+1
                    if c>cur: break
                    f2.append(cur - c)
            level +=1
            f1 = f2
        return -1
