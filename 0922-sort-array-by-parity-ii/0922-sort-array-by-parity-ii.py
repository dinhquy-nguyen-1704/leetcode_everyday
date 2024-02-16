class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        l1 = []
        l2 = []
        l = []

        for i in nums:
            if i%2 == 0:
                l1.append(i)

            else:
                l2.append(i)

        g = list(zip(l1, l2))

        for (a, b) in g:
            l.append(a)
            l.append(b)

        return l
