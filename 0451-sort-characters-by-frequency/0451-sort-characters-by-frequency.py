class Solution:
    def frequencySort(self, s: str) -> str:

        lst = [0]*80

        for i in s:
            pos = ord(i) - ord("0")
            lst[pos] += 1

        dic = {i: lst[ord(i) - ord("0")] for i in s}

        l = sorted(dic.items(), key=lambda dic:dic[1])
        k = len(l)
        st = ""
        for i in range(k):
            st += l[k - i - 1][0]*l[k - i - 1][1]

        return st