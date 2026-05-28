class Solution:
    def findDuplicates(self, arr):
        # code here
        freq_dict = {}
        dup_lst = []
        for num in arr:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        for key, value in freq_dict.items():
            if value > 1:
                dup_lst.append(key)
        return dup_lst