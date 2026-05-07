#User function Template for python3
class Solution:
	
	def findSum(self,arr):
		# code here
		st = set()
		sum = 0
		for num in arr:
		    if num not in st:
		        sum += num
		        st.add(num)
	    return sum
		        