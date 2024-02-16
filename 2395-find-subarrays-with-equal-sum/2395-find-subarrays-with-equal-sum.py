class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        l = len(nums)

        lst = [nums[i]+nums[i+1] for i in range(l-1)]

        s = set(lst)

        return len(s) != l-1