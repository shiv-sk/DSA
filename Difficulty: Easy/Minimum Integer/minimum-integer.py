import math
class Solution:
    def minimumInteger(self, arr):
        # code here
        n = len(arr)
        total_sum = sum(arr)
        ans = math.inf
        for num in arr:
            if total_sum <= n * num:
                ans = min(ans, num)
        return ans