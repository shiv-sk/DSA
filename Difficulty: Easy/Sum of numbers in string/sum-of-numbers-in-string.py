class Solution:
    def findSum(self, s):
        #code here
        total_sum = 0
        current_sum = 0
        for char in s:
            if char.isdigit():
                current_sum = current_sum * 10 + int(char)
            else:
                total_sum = total_sum + current_sum
                current_sum = 0
        total_sum = total_sum + current_sum
        return total_sum