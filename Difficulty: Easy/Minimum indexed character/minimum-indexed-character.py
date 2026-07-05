class Solution:
    def minIndexChar(self,s1,s2): 
        #code here
        s2_map = {}
        for char in s2:
            s2_map[char] = s2_map.get(char, 1) + 1
        for i in range(len(s1)):
            if s1[i] in s2_map:
                return i
        return -1