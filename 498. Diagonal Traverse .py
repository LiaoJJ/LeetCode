'''

solution 1: O(n^2)
using hashmap to store, observing that the key = i+j
and also reverse even one
https://leetcode.com/problems/diagonal-traverse/discuss/97767/Simply-Python-Solution

solution: just walk O(n^2), complex logic
https://leetcode.com/problems/diagonal-traverse/discuss/97711/Java-15-lines-without-using-boolean

'''

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix)==0: return []
        c = collections.defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):
                c[i+j].append(matrix[i][j])
        for i in range(m+n-1):
            if i%2==0: c[i].reverse()
            res += c[i]
        return res