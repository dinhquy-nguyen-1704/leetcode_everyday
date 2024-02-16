class Solution:
    def longestPalindrome(self, s: str) -> int:

        s_new = list(set(s))

        c = 0
        so_le = 0

        for i in s_new:
            k = s.count(i)
            if k%2 == 0:
                c += k
            else:
                c += k - 1 
                so_le = 1
                
        if so_le == 1:
            return c + 1
        else:
            return c