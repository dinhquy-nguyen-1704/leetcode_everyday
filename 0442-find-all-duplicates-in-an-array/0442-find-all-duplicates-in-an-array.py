class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l = [0]*(n+1)

        for i in nums:
            l[i] += 1

        ans = []
        for i in range(n+1):
            if l[i] > 1:
                ans.append(i)

        return ans