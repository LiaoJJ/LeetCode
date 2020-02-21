'''
BF O(n^3)
prefix Sum O(n^2)

hashtable O(n)
since the problem ask to get the longest length, which sums to k
so change the input, into a hashtable {currentSum: index}
and check the index of (currentSum - k), this will lead to longest subarray sums to k, ending in this index

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77784/O(n)-super-clean-9-line-Java-solution-with-HashMap
'''


class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums or len(nums)==0: return 0
        mp = {0:-1}
        acc = 0
        res = 0
        for i,num, in enumerate(nums):
            acc += num
            if acc-k in mp:
                res = max(res, i - mp[acc-k] + 1)
            if acc not in mp:
                mp[acc] = i
        return res