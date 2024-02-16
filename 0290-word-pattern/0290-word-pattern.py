class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        ls = s.split()
        l1 = []
        l2 = []

        for i in pattern:
            l1.append(pattern.index(i))

        for j in ls:
            l2.append(ls.index(j))

        len1 = len(l1)

        if len1 != len(l2):
            return False
        else:
            for i in range(len1):
                if l1[i] != l2[i]:
                    return False

            return True