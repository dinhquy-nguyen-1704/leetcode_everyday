class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        l = len(arr)
        lst = [arr[i+1] - arr[i] for i in range(l-1)]
        fi = set(lst)

        return len(fi) == 1