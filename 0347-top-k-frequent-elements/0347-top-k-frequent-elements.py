class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        l = list(sorted(dic.items(), key = lambda x:x[1]))
        le = len(l)
        lst = [l[le - i - 1][0] for i in range(k)]

        return lst