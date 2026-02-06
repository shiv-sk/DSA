#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        rev = ""
        for ch in s:
            rev = ch + rev
        return rev