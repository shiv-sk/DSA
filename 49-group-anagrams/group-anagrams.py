class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for ele in strs:
            key = ''.join(sorted(ele))
            if key in anagram_map:
                anagram_map[key].append(ele)
            else:
                anagram_map[key] = [ele]
        return list(anagram_map.values())