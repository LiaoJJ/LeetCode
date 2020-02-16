'''
hard for me, the key point is that the problem is guaranteed to have an answer, you don't need to consider too much. It's guaranteed

1. DFS, O(n^2)
https://www.youtube.com/watch?v=__yxFFRQAl8&t=647s

2. DP, O(n)
maintain 2 dp array, swap, not_swap
there are 3 cases at i-th index:
- you have to swap
- you have to not_swap
- you can either swap ot not_swap (this case is easy to omit)

https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/C%2B%2BJavaPython-DP-O(N)-Solution
'''

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        if not A or len(A)==0 or len(A)!=len(B): return 0
        n = len(A)
        swap = [n]*n
        swap[0] = 1
        not_swap = [n]*n
        not_swap[0] = 0
        for i in range(1, n):
            if A[i]>A[i-1] and B[i] > B[i-1]:
                swap[i] = swap[i-1] + 1
                not_swap[i] = not_swap[i-1]
            if A[i]>B[i-1] and B[i]>A[i-1]:
                swap[i] = min(swap[i], not_swap[i-1] + 1)
                not_swap[i] = min(not_swap[i], swap[i-1])
        return min(swap[n-1], not_swap[n-1])