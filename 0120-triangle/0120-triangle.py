class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def recur(n):

            if n == 1:
                return triangle[0]

            elif n == 2:
                return [triangle[0][0]+triangle[1][0], triangle[0][0]+triangle[1][1]]

            else:

                l = []
                l_old = recur(n-1)

                for i in range(n):
                    if i == 0:
                        l.append(l_old[0]+triangle[n-1][0])
                    elif i>0 and i<n-1:
                        l.append(min(l_old[i-1]+triangle[n-1][i], l_old[i]+triangle[n-1][i]))
                    else:
                        l.append(l_old[n-2]+triangle[n-1][n-1])

                return l

        n = len(triangle)
        return min(recur(n))

