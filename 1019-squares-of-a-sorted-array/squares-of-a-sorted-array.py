class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            square_of_num = nums[i] * nums[i]
            nums[i] = square_of_num
        nums.sort()
        return nums