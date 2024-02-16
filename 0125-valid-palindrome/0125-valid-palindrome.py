class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        st = ''
        for i in s:
            if ord(i) in range(97, 123) or ord(i) in range(48, 58):
                st += i
        if st == st[::-1]:
            return True
        else:
            return False
        '''
        a = 0
        b = len(st) - 1
        while a <= b:
            if st[a] != st[b]:
                return False
            else:
                a += 1
                b -= 1
        return True
        '''