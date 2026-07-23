class Solution:
    def extraChar(self, s1, s2):
        # code here
        sum1 = sum(ord(c) for c in s1)
        sum2 = sum(ord(c) for c in s2)
        
        extra_ascii = abs(sum1 - sum2)
        return chr(extra_ascii)