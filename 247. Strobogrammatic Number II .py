'''
do this recursively
if n is odd, then insert one Strobogrammatic character in the middle
if n is even, then insert 2 Strobogrammatic character in the middle
be careful with the bug test case of n==2

'''

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        even = ["00", "11", "69", "96", "88"]
        odd = ["0", "1", "8"]
        if n==1: return odd
        if n==2: return even[1:]

        if n%2==0:
            pre = self.findStrobogrammatic(n-2)
            mid = (n-2)//2
            cand = even
        else:
            pre = self.findStrobogrammatic(n-1)
            mid = (n-1)//2
            cand = odd
        return [p[:mid] + c + p[mid:] for p in pre for c in cand]