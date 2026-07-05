class Solution:
    def firstRep(self, s):
        # code here
        repeating_char = {}
        for char in s:
            repeating_char[char] = repeating_char.get(char, 0) + 1
        for char in s:
            if repeating_char[char] > 1:
                return char
        return -1