'''
just a simple Range Sum problem
be careful that  "if i-1>=0 else 0" cannot be ommited, since there will be bug if input has only 1 row
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or len(matrix[0])==0: return
        m, n = len(matrix), len(matrix[0])
        self.Sum = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.Sum[i][j] = matrix[i][j]\
                            + (self.Sum[i-1][j] if i-1>=0 else 0)\
                            + (self.Sum[i][j-1] if j-1>=0 else 0)\
                            - (self.Sum[i-1][j-1] if i-1>=0 and j-1>=0 else 0)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # print(self.Sum)
        return self.Sum[r2][c2]\
                 - (self.Sum[r2][c1-1] if c1-1>=0 else 0)\
                - (self.Sum[r1-1][c2] if r1-1 >=0 else 0)\
                + (self.Sum[r1-1][c1-1] if r1-1>=0 and c1-1>=0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)