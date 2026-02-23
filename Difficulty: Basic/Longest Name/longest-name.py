
class Solution:
    def longest(self, arr):
        # code here
        max_len_str = arr[0]
        for val in arr:
            if len(val) > len(max_len_str):
                max_len_str = val
        return max_len_str