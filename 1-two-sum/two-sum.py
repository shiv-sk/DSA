class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in num_map:
                return [num_map[num2], i]
            num_map[nums[i]] = i