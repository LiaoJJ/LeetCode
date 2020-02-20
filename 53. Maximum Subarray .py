'''
Greedy O(n)
find the local maximum ends exactly at each index
then find the maximum one

be careful with corner cases [-1]
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums)==0: return 0
        local, globald = float('-inf'), float('-inf')
        for num in nums:
            local = max(num, local + num)
            globald = max(globald, local)
        return globald