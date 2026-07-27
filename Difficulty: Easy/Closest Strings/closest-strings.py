class Solution:
	def shortestDistance(self, s, word1, word2):
		# code here
		word1_index = -1 
		word2_index = -1 
		minimum_distance = float('inf')
		for i in range(len(s)):
		    if s[i] == word1:
		        word1_index = i
		    elif s[i] == word2:
		        word2_index = i
		    if word1_index != -1 and word2_index != -1:
		        distance = abs(word1_index - word2_index)
		        minimum_distance = min(minimum_distance, distance)
		return minimum_distance if minimum_distance != float('inf') else 0