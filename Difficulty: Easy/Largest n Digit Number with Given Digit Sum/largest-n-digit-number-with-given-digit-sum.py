class Solution:
    def largestNumber(self, n, s):
        # code here
        result = []
        if s == 0:
            return "0" * n
        if s > 9 * n:
            return "-1"
        for i in range(n):
            digit = min(9, s)
            result.append(str(digit))
            s -= digit
        return "".join(result)