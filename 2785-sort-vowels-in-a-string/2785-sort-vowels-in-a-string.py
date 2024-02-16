class Solution:
    def sortVowels(self, s: str) -> str:

        lst = list(s)
        l = []
        n = len(lst)

        for i in range(n):
            if lst[i] in ["A", "E", "O", "U", "I", "a", "e", "o", "u", "i"]:
                l.append(lst[i])
                lst[i] = 0


        l.sort(reverse = True)

        for i in range(n):
            if lst[i] == 0:
                k = l.pop()
                lst[i] = k

        return "".join(lst)

