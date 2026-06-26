#User function Template for python3

class Solution:
    def calc_Sum (self, arr1, arr2) : 
        #Complete the function
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry > 0:
            current_sum = carry
            if i >= 0:
                current_sum += arr1[i]
                i -= 1
            if j >= 0:
                current_sum += arr2[j]
                j -= 1
            digit = current_sum % 10
            carry = current_sum // 10
            result.append(digit)
        result.reverse()
        return "".join(str(digit) for digit in result)