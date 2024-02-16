class Solution(object):
    def plusOne(self, digits):
        st = ''
        for i in digits:
            st += str(i)

        num = int(st) + 1

        num_str = str(num)

        out = [int(i) for i in num_str]

        return out
