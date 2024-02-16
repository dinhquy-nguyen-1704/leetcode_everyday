class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if nums[0] >= 0:
            return [i*i for i in nums]

        elif nums[-1] <= 0:
            l = []
            for i in range(n):
                l.append(nums[n-i-1]*nums[n-i-1])
            return l

        else:

            for i in range(n-1):
                if nums[i] < 0 and nums[i+1] >= 0:
                    x = i
                    y = i+1
                    break

            ans = []
            while x >= 0 and y <= n-1:
                if -nums[x] <= nums[y]:
                    ans.append(nums[x]*nums[x])
                    x = x - 1
                else:
                    ans.append(nums[y]*nums[y])
                    y = y + 1

            if x == -1:
                while y != n:
                    ans.append(nums[y]*nums[y])
                    y = y + 1

            if y == n:
                while x != -1:
                    ans.append(nums[x]*nums[x])
                    x = x - 1

            return ans


        