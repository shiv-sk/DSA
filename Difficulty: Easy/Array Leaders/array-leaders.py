class Solution:
    def leaders(self, arr):
        # code here
        ans = []
        size = len(arr)
        current_max = arr[size - 1]
        ans.append(current_max)
        for i in range(size - 2, -1, -1):
            if arr[i] >= current_max:
                ans.append(arr[i])
                current_max = arr[i]
        ans.reverse()
        return ans