class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        s = list(set(nums))

        for i in s:
            while nums.count(i) > 2:
                nums.remove(i)

        return len(nums)
        '''

        k = 0
        for i in nums:
            if k < 2 or i != nums[k-2]:
                nums[k] = i
                k += 1

        return k