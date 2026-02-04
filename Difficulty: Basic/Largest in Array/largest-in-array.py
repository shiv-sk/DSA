class Solution:
    def largest(self, arr):
        # code here
        largest_number = 0
        for num in arr:
            if num > largest_number:
                largest_number = num
        return largest_number
        
