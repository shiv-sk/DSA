class Solution:
    def twoSum(self, arr, target):
        #code here
        freq = {}
        for i in range(len(arr)):
            compliment = target - arr[i]
            if compliment in freq:
                return [freq[compliment] + 1, i + 1]
            freq[arr[i]] = i
        return [-1, -1]