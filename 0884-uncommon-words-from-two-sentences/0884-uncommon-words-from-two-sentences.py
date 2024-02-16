class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1l = s1.split()
        s2l = s2.split()

        s1d = {}
        for i in s1l:
            if i not in s1d:
                s1d[i] = 1
            else:
                s1d[i] += 1

        s2d = {}
        for i in s2l:
            if i not in s2d:
                s2d[i] = 1
            else:
                s2d[i] += 1      

        l = []
        for i in s1d:
            if s1d[i] == 1 and i not in s2d:
                l.append(i)

        for i in s2d:
            if s2d[i] == 1 and i not in s1d:
                l.append(i)

        return l
