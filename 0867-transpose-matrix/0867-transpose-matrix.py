import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m = np.array(matrix)

        n = m.T

        return n.tolist()