class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_str = {}
        for char in s:
            unique_str[char] = unique_str.get(char, 0) + 1
        for i in range(len(s)):
            if unique_str[s[i]] == 1:
                return i
        return -1