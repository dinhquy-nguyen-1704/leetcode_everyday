class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lp = len(part)
        flag = 1
        while flag == 1:
            ls = len(s)
            if ls >= lp:
                for i in range(ls-lp+1):
                    if s[i:i+lp] == part:
                        s = s[:i] + s[i+lp:]
                        flag = 1
                        print(s)
                        break
                    flag = 0
            else:
                flag = 0
        return s