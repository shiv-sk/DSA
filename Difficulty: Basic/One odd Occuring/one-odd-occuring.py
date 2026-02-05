class Solution:
    def getOddOccurrence(self, arr):
        # code here
        frequency_dict = {}
        for num in arr:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1
        for key, value in frequency_dict.items():
            if value%2 != 0:
                return key
        return -1