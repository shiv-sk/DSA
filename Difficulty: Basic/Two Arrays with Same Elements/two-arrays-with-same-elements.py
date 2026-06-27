class Solution:
    def isIdentical(self, a, b):
        # code here
        a.sort()
        b.sort()
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True