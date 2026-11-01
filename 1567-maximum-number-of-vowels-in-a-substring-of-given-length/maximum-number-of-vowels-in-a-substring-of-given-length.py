class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        left = 0
        vowels = "aeiou"
        max_count = 0
        for right in range(len(s)):
            if s[right] in vowels:
                vowel_count += 1
            if right - left + 1 == k:
                max_count = max(vowel_count, max_count)
                if s[left] in vowels:
                    vowel_count -= 1
                left += 1
        return max_count