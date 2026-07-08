class Solution:
    def repeatingCharacter(self,s):
        #code here
        repeating_chars = {}
        for char in s:
            repeating_chars[char] = repeating_chars.get(char, 0) + 1
        for i in range(len(s)):
            if repeating_chars[s[i]] > 1:
                return i
        return -1