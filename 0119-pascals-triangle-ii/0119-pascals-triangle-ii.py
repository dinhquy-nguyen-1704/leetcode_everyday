class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        l = [[] for _ in range(rowIndex+1)]
        l[0].append(1)
        l[1] = l[1] + [1, 1]

        for i in range(2, rowIndex+1):
            l[i].append(1)
            for j in range(1, i):
                l[i].append(l[i-1][j-1] + l[i-1][j])
            l[i].append(1)

        return l[-1]