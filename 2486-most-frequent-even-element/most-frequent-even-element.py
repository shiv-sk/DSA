class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        max_count = 0
        max_element = -1
        num_map = {}
        for num in nums:
            if num % 2 == 0:
                num_map[num] = num_map.get(num, 0) + 1
            count = num_map.get(num, 0)
            if count > max_count:
                max_count = count
                max_element = num
            elif count == max_count:
                if max_element > num:
                    max_element = num
        return max_element