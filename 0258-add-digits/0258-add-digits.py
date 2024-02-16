class Solution:
    def addDigits(self, num: int) -> int:

        while len(str(num)) > 1:
            n = 0
            for i in str(num):
                n += int(i)

            num = n

        return num
