class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_map = {}
        if len(s) != len(t):
            return False
        # for char in s:
        #     s_map[char] = s_map.get(char, 0) + 1
        # for char in t:
        #     if char in s_map and s_map[char] > 0:
        #         s_map[char] -= 1
        #     else:
        #         return False
        # return True
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True