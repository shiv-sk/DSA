#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        arr.sort()
        previous_number = -1
        for num in arr:
            if previous_number == num:
                return num
            else:
                previous_number = num