'''
the harder version of 239
BF O(nklgk)

Binary Search and insert delete O(nk)

using 2 heap, a max heap for small value, a min heap for large value
be careful with that: the size of min heap and max heap may not be balanced, because of lazy delete. But the result is still correct.
https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps

'''

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        