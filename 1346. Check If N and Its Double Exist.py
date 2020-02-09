class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        memo = set()
        for a in arr:
            if a in memo: return True
            if a%2==0:
                memo.add(a//2)
            memo.add(a*2)
        return False