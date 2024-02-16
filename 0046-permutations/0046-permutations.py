class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def insertAll(A, n):
            new = []

            for i in range(len(A)+1):
                B = A.copy()
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

        return generate(nums)
            