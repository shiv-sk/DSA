class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        st = set(jewels)
        count = 0
        for char in stones:
            if char in st:
                count += 1
        return count