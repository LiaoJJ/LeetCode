'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93719/Greedy-Python-(132-ms)

Greedy O(nlgn) O(1)
when seeing intervals problems, you should consider sort by ending point.
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res, prev = 0, float('-inf')
        for x, y in points:
            if x <= prev:
                continue
            prev = y
            res+=1
        return res