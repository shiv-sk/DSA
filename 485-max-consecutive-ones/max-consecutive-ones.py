class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        consecutive_ones = 0
        for i in range(len(nums)):
           
            if nums[i] == 1:
                consecutive_ones += 1
                max_ones = max(max_ones, consecutive_ones)
            else:
                consecutive_ones = 0
        return max_ones