class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        dic = {}

        m = len(mat)
        for i in range(m):
            dic[i] = sum(mat[i])

        l = sorted(dic, key = lambda i:dic[i])

        return l[:k]