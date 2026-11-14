class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # ans = []
        # for i in range(len(temperatures)):
        #     distance = 0
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             distance = j - i
        #             break
        #     ans.append(distance)
        # return ans
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                distance = i - prev_index
                ans[prev_index] = distance
            stack.append(i)
        return ans