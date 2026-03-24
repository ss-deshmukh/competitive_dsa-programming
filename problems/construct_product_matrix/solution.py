class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        result = [[0] * m for i in grid]
        mod = 12345
        pre = 1
        for i in range(n):
            for j in range(m):
                result[i][j] = pre
                pre = (pre * grid[i][j]) % mod
        post = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                result[i][j] = (post * result[i][j]) % mod
                post = (post * grid[i][j]) % mod
        return result
