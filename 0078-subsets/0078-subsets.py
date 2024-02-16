class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recur(nums):
            if len(nums) == 1:
                return [[], nums]
            else:
                a = recur(nums[:-1])
                l = len(a)
                for i in range(l):
                    k = a[i].copy()
                    k.append(nums[-1])
                    a.append(k)

                return a

        return recur(nums)
