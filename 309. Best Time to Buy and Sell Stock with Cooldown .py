class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        s1, s2, s3 = 0, float('-inf'), 0
        for price in prices:
            temp1 = max(s1, s3)
            temp2 = max(s2, s1 - price)
            temp3 = s2 + price
            s1, s2, s3 = temp1, temp2, temp3
        return max(s1, s3)