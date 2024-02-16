class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        l = len(startTime)
        c = 0

        for i in range(l):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                c += 1

        return c