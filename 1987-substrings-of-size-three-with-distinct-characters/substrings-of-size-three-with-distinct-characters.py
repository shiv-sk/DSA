class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            sub_set = set()
            sub_set.add(s[i])
            sub_set.add(s[i + 1])
            sub_set.add(s[i + 2])

            if len(sub_set) == 3:
                count += 1
        return count