class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        l = len(nums)
        c = 0

        for i in range(l):
            for j in range(l):
                if i == j:
                    continue

                else:
                    if nums[i] + nums[j] == target:
                        c += 1

        return c