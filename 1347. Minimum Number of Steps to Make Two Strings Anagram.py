class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s)!=len(t): return -1
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        res = 0
        for i in set(list(c1.keys()) + list(c2.keys())):
            res += abs(c1[i] - c2[i])
        return res//2;