class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_side_sum = 0
        for i in range(len(nums)):
            right_side_sum = total_sum - left_side_sum - nums[i]
            if right_side_sum == left_side_sum:
                return i
            left_side_sum += nums[i]
        return -1  