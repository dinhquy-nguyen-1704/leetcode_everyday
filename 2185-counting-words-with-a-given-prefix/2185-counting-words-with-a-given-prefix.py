class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        l = len(pref)

        lst = [i for i in words if i[:l] == pref]

        return len(lst)