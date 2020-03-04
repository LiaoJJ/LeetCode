'''
the same as Meeting Room
scan from left to right, 
for every point if it's a start point, add up # of passengers
                if it's a end point, substract # pf passengers
                if the capacity below 0, return False
O(length) or O(nlgn)
https://leetcode.com/problems/car-pooling/discuss/317611/C%2B%2BJava-O(n)-Thousand-and-One-Stops
'''


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips: return False
        table = [0]*(1001)
        for num, start, end in trips:
            table[start] += num
            table[end]   += -num
        for i in range(1001):
            capacity -=table[i]
            if capacity<0: return False
        return True