class Solution(object):
    def mySqrt(self, x):
        a = x
        while (a*a - x) > 0.01:
            a = (a + x/a)/2

        return int(a)