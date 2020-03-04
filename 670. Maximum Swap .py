'''
my: 
1. find the turn point
2. find the last biggest number after turn point
3. swap biggest with first number that's smaller than it
be careful with many corner cases: >=, <

another 2 better solution:

1. scan from right to left, find maximum and the last one that is smaller than this maximum
https://leetcode.com/problems/maximum-swap/discuss/107073/C%2B%2B-one-pass-simple-and-fast-solution%3A-1-3ms-O(n)-time

2. find the largest number that's behind current one
https://leetcode.com/problems/maximum-swap/discuss/107068/Java-simple-solution-O(n)-time
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num==None: return -1
        num = list(map(int, str(num)))
        n = len(num)

        # find the turn point
        i=0
        while i<n-1:
            if num[i] < num[i+1]: break
            i+=1
        # find the last biggest after turn point
        biggest = [i, num[i]]
        for j in range(i+1, n):
            if num[j] >= biggest[1]:
                biggest = [j, num[j]]

        # swap biggest with first below it
        for k in range(0, i+1):
            if num[k] < biggest[1]:
                num[biggest[0]], num[k] = num[k], num[biggest[0]]
                break
        return int("".join(map(str, num)))
