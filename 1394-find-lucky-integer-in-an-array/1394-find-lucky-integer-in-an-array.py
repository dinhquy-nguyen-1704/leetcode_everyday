class Solution:
    def findLucky(self, arr: List[int]) -> int:

        s = list(set(arr))
        s.sort(reverse = True)

        for i in s:
            if arr.count(i) == i:
                return i

        return -1