'''
using Counter to get freq.
and using prefixSum to get total number by O(1)
the range of friend request for A is (0.5*age[A]+7, age[A]]
O(n) O(n)
https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127341/10ms-concise-Java-solution-O(n)-time-and-O(1)-space
'''

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages: return 0
        freq = [0]*121
        res = 0

        for age in ages: 
            freq[age] += 1
        sumf = freq[:]
        for i in range(1, 121):
            sumf[i] += sumf[i-1]
        for i in range(15, 121):
            left = i//2 + 7
            right = i
            total = sumf[right] - sumf[left]
            res += (total-1) * freq[i]
        return res
