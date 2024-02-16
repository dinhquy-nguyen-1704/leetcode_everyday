class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def insertAll(nums, n):
            new = []

            for i in range(len(nums)+1):
                B = nums.copy()
                B.insert(i, n)
                new.append(B)

            return new

        def generate(nums):
            if len(nums) == 1:
                return [nums]
            else:
                new = []
                A = generate(nums[:-1])
                for p in A:
                    new = new + insertAll(p, nums[-1]) 

                return new

        ans1 = generate(nums)
        ans2 = []
        for i in ans1:
            if i not in ans2:
                ans2.append(i)
        
        return ans2
