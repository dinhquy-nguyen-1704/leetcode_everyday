class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        dp = [nums[0]]
        l = len(nums)
        for i in range(l-1):
            dp.append(dp[i]+nums[i+1])

        return dp