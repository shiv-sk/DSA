class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = word.find(ch)
        string = ""
        if ch_index != -1:
            prefix = word[: ch_index + 1]
            return prefix[::-1] + word[ch_index + 1:]
        return word
        