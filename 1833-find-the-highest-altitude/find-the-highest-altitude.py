class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        start = 0
        for alt in gain:
            start += alt
            highest_altitude = max(highest_altitude, start)
        return highest_altitude