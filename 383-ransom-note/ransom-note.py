class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        for char in magazine:
            mag_map[char] = mag_map.get(char, 0) + 1
        for char in ransomNote:
            if char in mag_map and mag_map[char] > 0:
                mag_map[char] -= 1
            else:
                return False
        return True