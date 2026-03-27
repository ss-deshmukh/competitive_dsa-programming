class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        m = len(mat)
        n = len(mat[0])
        new_mat = [[0] * n for i in range(m)]  # O(mn)
        steps = k % n

        # O(mn)
        for i in range(0, m, +2):
            for j in range(n):
                new_mat[i][j - steps] = mat[i][j]
                # negative indices autohandled by python
        for i in range(1, m, +2):
            for j in range(n):
                nj = j + steps
                new_mat[i][nj if nj <= n - 1 else (nj - n)] = mat[i][j]
                # handling out of bounds indices

        return mat == new_mat
