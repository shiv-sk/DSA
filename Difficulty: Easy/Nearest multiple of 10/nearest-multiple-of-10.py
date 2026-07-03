class Solution:
    def roundToNearest (self, s) : 
        last_digit = int(s[-1])
        
        if last_digit == 0:
            return s
        elif last_digit <= 5:
            return s[:-1] + '0'
        else:
            front_list = list(s[:-1])
            carry = 1
            i = len(front_list) - 1
            
            while i >= 0 and carry > 0:
                current_digit = int(front_list[i])
                total = current_digit + carry
                
                front_list[i] = str(total % 10)
                carry = total // 10
                i -= 1
            
            # FIX: Check if carry survived AFTER the loop finishes entirely
            if carry > 0:
                return "1" + "".join(front_list) + "0"
            
            return "".join(front_list) + "0"