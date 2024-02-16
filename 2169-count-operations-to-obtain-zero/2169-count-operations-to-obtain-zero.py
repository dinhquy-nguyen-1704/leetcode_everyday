class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        if num1 == 0 or num2 == 0:
            return 0
            
        ans = 1
        while num1 != num2:
            if num1 < num2:
                num2 = num2 - num1

            else:
                num1 = num1 - num2

            ans += 1

        return ans