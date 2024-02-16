class Solution(object):
    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()
        return nums.index(target)