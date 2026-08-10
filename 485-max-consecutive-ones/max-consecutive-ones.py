class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        consecutive_ones = 0
        for i in range(len(nums)):
           
            if nums[i] == 1:
                consecutive_ones += 1
            else:
                max_ones = max(max_ones, consecutive_ones)
                consecutive_ones = 0
        return max(max_ones,  consecutive_ones)