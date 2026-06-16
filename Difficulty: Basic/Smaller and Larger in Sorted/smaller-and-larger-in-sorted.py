class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        larger_num = 0 
        smaller_num = 0
        for num in arr:
            if num >= target:
                larger_num += 1
            if num <= target:
                smaller_num += 1
        return [smaller_num, larger_num]