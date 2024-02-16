class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        l = len(s)
        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))

        for i in range(l):
            if map1[i] != map2[i]:
                return False
        return True
