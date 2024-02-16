class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 1000

        nums.sort()

        c = 0
        for i in nums:
            if i != 1000:
                c += 1

        return c