class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for ele in operations:
            if ele == "C":
                stack.pop()
            elif ele == "D":
                prev_ele = stack[-1]
                new_ele = 2 * prev_ele
                stack.append(new_ele)
            elif ele == "+":
                new_ele = stack[-1] + stack[-2]
                stack.append(new_ele)
            else:
                stack.append(int(ele))
        return sum(stack)