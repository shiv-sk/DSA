class Solution:
    def arrangeString(self, s):
        # code here
        total_sum = 0
        string = ""
        for char in s:
            if char.isdigit():
                total_sum += int(char)
            else:
                string += char
        sorted_letters = "".join(sorted(string))
        if total_sum:
            return sorted_letters + str(total_sum)
        else:
            return sorted_letters
        