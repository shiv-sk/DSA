class Solution:
    def sameSeq(self, s1, s2):
        # code here
        i = 0
        j = 0
        n = len(s1)
        m = len(s2)
        while i < n and j < m:
            if s1[i] != s2[j]:
                return False
            char = s1[i]
            while i < n and s1[i] == char:
                i += 1
            while j < m and s2[j] == char:
                j += 1
        return i == n and j == m