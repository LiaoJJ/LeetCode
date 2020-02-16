'''
follow-up to 198
the only problem we need to solve is the conflict of A[0] and A[n-1], divide it into 2 variable, [0:n-1], and [1:n]
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def help(nums, left, right):
            n = right - left + 1
            prev1, prev2 = 0, 0
            for i in range(left, right+1):
                temp = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, temp
            return prev1
        if not nums or len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        n = len(nums)
        return max(
            help(nums, 0, n-2),
            help(nums, 1, n-1)
        )
            