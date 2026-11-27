from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        for char in t:
            if s_counter[char] == 0:
                return char
            s_counter[char] -= 1