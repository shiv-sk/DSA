class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_side_sum = 0
        for i in range(len(nums)):
            right_side_sum = total - left_side_sum - nums[i]
            if left_side_sum == right_side_sum:
                return i
            left_side_sum += nums[i]
        return -1