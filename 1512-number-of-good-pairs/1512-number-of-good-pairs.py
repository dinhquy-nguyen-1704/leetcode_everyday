class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        s = list(set(nums))
        count = 0

        for i in s:
            c = nums.count(i)
            if c > 1:
                count += c*(c-1)/2

        return int(count)