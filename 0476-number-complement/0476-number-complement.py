class Solution:
    def findComplement(self, num: int) -> int:
        st = ""
        while num != 0:
            st += str(num%2)
            num = num//2

        st2 = ""
        for i in st:
            if i == "0":
                st2 += "1"
            else:
                st2 += "0"

        dec = 0
        for j in range(len(st2)):
            if st2[j] == "1":
                dec += 2**(j)

        return dec


