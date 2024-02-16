class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic1 = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        dic2 = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        num1_l = list(num1)
        num2_l = list(num2)
        x = 0
        y = 0
        for i in num1_l:
            x = x*10+dic1[i]

        for i in num2_l:
            y = y*10+dic1[i]

        z = x + y
        m = []
        
        if z == 0:
            return "0"

        while z != 0:
            m.append(dic2[z%10])
            z = z//10

        m = m[::-1]
        return "".join(m)

        

