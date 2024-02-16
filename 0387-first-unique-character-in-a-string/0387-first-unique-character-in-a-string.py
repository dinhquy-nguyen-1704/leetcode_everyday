class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        c = 0
        for i in s:
            if dic[i] != 1:
                c += 1
            else:
                return c

        return -1
