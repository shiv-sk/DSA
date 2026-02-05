#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        for i, num in enumerate(arr):
            if num == 1:
                return i
        return -1
    # Your code goes here
    

