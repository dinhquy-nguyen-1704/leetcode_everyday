class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        l1 = []
        l2 = []
        l3 = []

        for i in nums:
            if i < pivot:
                l1.append(i)

            elif i > pivot:
                l2.append(i)

            else:
                l3.append(i)

        return l1 + l3 + l2