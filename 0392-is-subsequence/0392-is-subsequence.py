class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        while len(s) > 0:
            if s[0] not in t:
                return False
            else:
                i = t.index(s[0])
                s = s[1:]
                t = t[i+1:]

        return True
        