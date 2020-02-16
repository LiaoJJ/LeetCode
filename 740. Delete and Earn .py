'''
observing that if you choose 3, you can take all 3 and you cannot take 2 or 4
this problem can be transfer to 198. House Robber 
https://leetcode.com/problems/delete-and-earn/discuss/109871/Awesome-Python-4-liner-with-explanation-Reduce-to-House-Robbers-Question-U0001f31d
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        counter = collections.Counter(nums)
        cur, prev = 0, 0
        for i in range(max(nums)+1):
            cur, prev = max(prev + counter[i] * i, cur), cur
        return cur