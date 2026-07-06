class Solution:
	def printString(self, s, ch, count):
		# code here
		char_count = 0
		for i in range(len(s)):
		    if s[i] == ch:
		        char_count += 1
		        if char_count == count:
		            return s[i + 1:]
		return ""
		            
		