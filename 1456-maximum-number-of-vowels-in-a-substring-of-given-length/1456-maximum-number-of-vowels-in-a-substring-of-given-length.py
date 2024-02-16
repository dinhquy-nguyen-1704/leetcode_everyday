class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s_lst = []

        for i in s:
            if i in ["a", "e", "o", "u", "i"]:
                s_lst.append(1)
            else:
                s_lst.append(0)

        su = sum(s_lst[:k])
        mx = su

        for j in range(1, len(s) - k + 1):
            su = su - s_lst[j-1] + s_lst[j+k-1]
            if su > mx:
                mx = su

        return mx


        