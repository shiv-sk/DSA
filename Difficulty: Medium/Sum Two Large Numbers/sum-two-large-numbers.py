class Solution:
	def findSum(self, s1, s2):
		# code here
		i = len(s1) - 1
		j = len(s2) - 1
		carry = 0
		result_digits = []
		while i >= 0 or j >= 0 or carry:
		    digit1 = int(s1[i]) if i >= 0 else 0
		    digit2 = int(s2[j]) if j >= 0 else 0
		    current_sum = digit1 + digit2 + carry
		    carry = current_sum // 10
		    digit = current_sum % 10
		    result_digits.append(str(digit))
		    i -= 1
		    j -= 1
		ans = "".join(result_digits[::-1])
		ans = ans.lstrip('0')
		return ans if ans else "0"