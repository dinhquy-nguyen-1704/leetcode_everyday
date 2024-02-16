class Solution(object):
    def addBinary(self, a, b):

        a_dec = 0
        b_dec = 0

        for i in range(len(a)):
            a_dec += int(a[-i-1])*2**(i)
        for j in range(len(b)):
            b_dec += int(b[-j-1])*2**(j)

        sum = a_dec + b_dec
        stack = []

        if sum == 0:
            return "0"

        while sum > 0:
            stack.append(sum%2)
            sum = sum//2

        sum_str = ''
        while stack != []:
            sum_str += str(stack.pop())

        return sum_str


