class Solution:
    def patternCount(self, S): 
        # code here 
        pattern = 0
        for i in range(len(S)):
            if S[i] == "1":
                j = i + 1
                while j < len(S) and S[j] == "0":
                    j += 1
                if j < len(S) and S[j] == "1" and j > i + 1:
                    pattern += 1
        return pattern