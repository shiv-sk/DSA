import math
class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        smallest = math.inf
        second_smallest = math.inf
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num > smallest:
                second_smallest = num
        if second_smallest == math.inf:
            return [-1]
        return [smallest, second_smallest]
        
