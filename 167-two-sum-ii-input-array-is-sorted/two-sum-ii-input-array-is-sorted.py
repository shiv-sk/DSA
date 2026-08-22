class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            sum_of_numbers = nums[left] + nums[right]
            if sum_of_numbers == target:
                return [left + 1 , right + 1]
            elif sum_of_numbers > target:
                right -= 1
            else:
                left += 1