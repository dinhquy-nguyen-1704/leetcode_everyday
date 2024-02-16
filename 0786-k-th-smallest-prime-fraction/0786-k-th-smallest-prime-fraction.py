class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        n = len(arr)
        l = []
        dic = {}

        for i in range(n-1):
            for j in range(i+1, n):
                l.append(arr[i]/arr[j])
                dic[arr[i]/arr[j]] = [arr[i], arr[j]]

        l.sort()
        return dic[l[k-1]]
