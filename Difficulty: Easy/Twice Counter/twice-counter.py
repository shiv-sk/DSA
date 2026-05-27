class Solution:
    def countWords(self, List):
        #code here
        freq = {}
        counter = 0
        for ele in List:
            freq[ele] = freq.get(ele, 0) + 1
        for val in freq.values():
            if val == 2:
                counter += 1
        return counter