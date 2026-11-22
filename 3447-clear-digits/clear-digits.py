class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        return "".join(stack)