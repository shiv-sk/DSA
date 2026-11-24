class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
            num_count = num_map.get(num)
            if num_count > len(nums) // 2:
                return num
        return -1