class Solution:
	def countOddEven(self, arr):
		#Code here
		odd = 0 
		even = 0
		for num in arr:
		    if num % 2 != 0:
		        odd += 1
		    else:
		        even += 1
		return (odd, even)