class Solution:
    def compressString(self, s: str) -> str:
        # code here
        s = s.lower()
        current_char = s[0]
        count = 0
        results = []
        for char in s:
            if char == current_char:
                count += 1
            else:
                results.append(f"{current_char}{count}")
                current_char = char
                count = 1
        results.append(f"{current_char}{count}")
        return "".join(results)