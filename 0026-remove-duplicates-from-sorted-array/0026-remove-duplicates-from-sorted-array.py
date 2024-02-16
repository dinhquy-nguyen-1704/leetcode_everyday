class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 1000
        
        nums.sort()

        c = 0
        for i in nums:
            if i != 1000:
                c += 1

        return c

