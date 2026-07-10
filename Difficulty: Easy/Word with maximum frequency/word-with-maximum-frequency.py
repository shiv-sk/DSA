class Solution:
    def maximumFrequency(self, s):
        # Your Code goes here
        words = s.split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        max_freq = 0
        max_freq_word = ""
        for word in words:
            if word_freq[word] > max_freq:
                max_freq = word_freq[word]
                max_freq_word = word
        return f"{max_freq_word} {max_freq}"