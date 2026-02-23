#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        new_str = ""
        for char in s:
            if char != " ":
                new_str += char
        return new_str