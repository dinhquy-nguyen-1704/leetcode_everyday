class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1 = []
        dic = {}
        l2 = [i for i in arr1 if i not in arr2]
        for i in arr1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i in arr2:
            l1 += [i]*dic[i]

        l2.sort()
        return l1+l2