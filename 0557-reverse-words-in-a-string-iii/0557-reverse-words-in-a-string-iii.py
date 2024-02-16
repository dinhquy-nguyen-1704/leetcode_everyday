class Solution:
    def reverseWords(self, s: str) -> str:

        lst = s.split()
        l = len(lst)

        for i in range(l):
            lst[i] = lst[i][::-1]


        st = " ".join(lst)

        return st