'''
O(n)
sort by 1st element
set the last one of res as compare, 
get the rightest most end each time

another idea O(nlgn)
sort begin and end respectly
and then constrct the res 
https://leetcode.com/problems/merge-intervals/discuss/21223/Beat-98-Java.-Sort-start-and-end-respectively.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals)==0: return []
        intervals.sort(key = lambda x:x[0])
        left, right = 0, 0
        res = [[float('-inf'), float('-inf')]]
        for i,j in intervals:
            if i > res[-1][1]:
                res.append([i,j])
            else:
                res[-1][1] = max(res[-1][1], j)
        res.pop(0)
        return res
                