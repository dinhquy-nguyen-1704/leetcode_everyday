class Solution:
    def countEven(self, num: int) -> int:

        c = 0
        for i in range(1, num+1):
            s = str(i)
            d = 0
            for j in s:
                d = d + int(j)
            if d%2 == 0:
                c += 1

        return c

