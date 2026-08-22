class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_str = []
        for char in s:
            if char.isalnum():
                pal_str.append(char.lower())
        ans = "".join(pal_str)
        i = 0
        j = len(ans) - 1
        while i <= j:
            if ans[i] != ans[j]:
                return False
            else:
                i += 1
                j -= 1
        return True