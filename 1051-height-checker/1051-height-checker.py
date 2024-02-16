class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        h = sorted(heights)
        n = len(heights)
        c = 0

        for i in range(n):
            if heights[i] != h[i]:
                c += 1

        return c