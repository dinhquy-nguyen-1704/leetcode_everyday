class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        if nums.count(0) == 0 or nums.count(0) == 1:
            return len(nums) - 1
        else:
            l = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    l.append(0)
                elif (nums[i] == 1 and i == 0) or (nums[i] == 1 and nums[i-1] == 0):
                    l.append(1)
                else:
                    l[-1] += 1

            m = 0
            for j in range(1, len(l)-1):
                if l[j-1] != 0 and l[j+1] != 0:
                    m = max(m, l[j-1]+l[j+1])
            mx = max(l)
            m = max(m, mx)

            return m
