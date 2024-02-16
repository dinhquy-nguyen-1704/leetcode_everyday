class Solution:
    def romanToInt(self, s: str) -> int:

        t = 0
        for i in range(len(s)):
            if i != len(s)-1 and s[i:i+2] == 'CM':
                t += 900
            elif i != len(s)-1 and s[i:i+2] == 'CD':
                t += 400
            elif i != len(s)-1 and s[i:i+2] == 'XC':
                t += 90
            elif i != len(s)-1 and s[i:i+2] == 'XL':
                t += 40
            elif i != len(s)-1 and s[i:i+2] == 'IX':
                t += 9
            elif i != len(s)-1 and s[i:i+2] == 'IV':
                t += 4
            elif s[i] == 'M' and (i == 0 or s[i-1] != 'C'):
                t += 1000
            elif s[i] == 'D' and (i == 0 or s[i-1] != 'C'):
                t += 500
            elif s[i] == 'C' and (i == 0 or s[i-1] != 'X'):
                t += 100
            elif s[i] == 'L' and (i == 0 or s[i-1] != 'X'):
                t += 50
            elif s[i] == 'X' and (i == 0 or s[i-1] != 'I'):
                t += 10
            elif s[i] == 'V' and (i == 0 or s[i-1] != 'I'):
                t += 5
            elif s[i] == 'I':
                t += 1

        return t

        