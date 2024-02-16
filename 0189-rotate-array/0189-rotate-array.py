class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        if l >= 2 and k != 0:
            l2 = nums[-k:]+nums[:l-k]
            nums.clear()
            for i in l2:
                nums.append(i)