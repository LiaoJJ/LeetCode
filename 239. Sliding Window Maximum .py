'''
Monotonic Queue O(n)
store index in the queue, if an older element in the queue is smaller than a newer element, then it's impossible to be result.

be careful to distinguish index and nums[index]
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)<k: return []
        queue = collections.deque()
        res = []
        n = len(nums)
        for i in range(n):
            # extend right
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            left = i-(k-1)
            if left<0: continue

            # shrink left
            if queue[0] < left:
                queue.popleft()

            # update result
            res.append(nums[queue[0]])
        return res
