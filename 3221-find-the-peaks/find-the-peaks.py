class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        if len(mountain) < 3:
            return []
        for peak in range(1, len(mountain) - 1):
            if mountain[peak] > mountain[peak-1] and mountain[peak] > mountain[peak + 1]:
                ans.append(peak)
        return ans