class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_distance = float('inf')
        left = 0
        win_sum = 0
        for right in range(len(nums)):
            win_sum += nums[right]
            while win_sum >= target:
                distance = right - left + 1
                min_distance = min(distance, min_distance)
                win_sum -= nums[left]
                left += 1
        return 0 if min_distance == float('inf') else min_distance