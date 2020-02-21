'''
need to be very calm to solve this kind of problem
should never confuse yourself, keep clear mind

there is only 2 cases:
1. there is idle:       using Counter to solve this case
2. there is no idle:    len(tasks)
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks or len(tasks)==0: return 0
        dic = collections.Counter(tasks)
        maxd = max(dic.values())
        num_of_maxd = 0
        for num in dic.values():
            if num==maxd: num_of_maxd += 1
        return max(
            len(tasks), # lower bound
            (maxd-1)*(n+1) + num_of_maxd # n is greater
        )