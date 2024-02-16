class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        g = (hour%12)*30+minutes/60 * 30
        p = minutes*6

        return min(abs(g-p), 360-abs(g-p))