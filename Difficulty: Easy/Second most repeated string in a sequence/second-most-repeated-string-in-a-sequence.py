class Solution:
    def secFrequent(self, arr):
        # code here
        freq_map = {}
        for s in arr:
            freq_map[s] = freq_map.get(s, 0) + 1
        max1_count, max1_word = -1, ""
        max2_count, max2_word = -1, ""
        
        for word, count in freq_map.items():
            if count > max1_count:
                max2_count = max1_count
                max2_word = max1_word
                max1_count = count
                max1_word = word
            elif count > max2_count and count < max1_count:
                max2_count = count
                max2_word = word
        return max2_count if max2_count != -1 else "-1"