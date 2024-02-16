class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        x = [True]
        mx = nums[0]

        for i in range(1, n):
            if mx >= i:
                x.append(True)
                mx = max(mx, i+nums[i])
            else:
                x.append(False)
                
        return x[n-1]
