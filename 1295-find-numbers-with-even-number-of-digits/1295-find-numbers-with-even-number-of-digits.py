class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        lst = [str(i) for i in nums]

        c = 0
        for i in lst:
            if len(i) % 2 == 0:
                c += 1

        return c