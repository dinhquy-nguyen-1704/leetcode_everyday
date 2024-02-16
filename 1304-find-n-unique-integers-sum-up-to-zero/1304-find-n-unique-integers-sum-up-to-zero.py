class Solution:
    def sumZero(self, n: int) -> List[int]:

        l = [i for i in range(1, n//2+1)]
        ans = [i for i in range(1, n//2+1)]

        for i in l:
            ans.append(-i)

        if n%2 == 0:
            return ans
        else:
            ans.append(0)
            return ans