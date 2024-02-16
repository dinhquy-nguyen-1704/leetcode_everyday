class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        st = str(n)
        tich = 1
        tong = 0

        for i in st:
            tich = tich*int(i)
            tong = tong + int(i)

        return tich - tong

        
