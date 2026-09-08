class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}
        word_list = s.split()

        if len(pattern) != len(word_list):
            return False
        
        for i in range(len(word_list)):
            if pattern[i] in pattern_to_s:
                if pattern_to_s[pattern[i]] != word_list[i]:
                    return False
            else:
                if word_list[i] in s_to_pattern:
                    return False
            s_to_pattern[word_list[i]] = pattern[i]
            pattern_to_s[pattern[i]] = word_list[i]
        return True