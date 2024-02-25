class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals_sorted = sorted(intervals, key=lambda x:x[0])

        n = len(intervals)

        mask = [0]*n

        output = []

        for i in range(n):
            if mask[i] == 1:
                continue
            else:
                mask[i] = 1
                a = intervals_sorted[i]

                for j in range(i+1, n):
                    if mask[j] == 1:
                        continue
                    else:
                        b = intervals_sorted[j]
                        if b[0] <= a[1]:
                            a = [a[0], max(a[1], b[1])]
                            mask[j] = 1

            output.append(a)

        return output