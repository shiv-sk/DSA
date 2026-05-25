#User function Template for python3

class Solution:
    def findDiff(self, arr):
        # code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        return max(freq.values()) - min(freq.values())