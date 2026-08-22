class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     square_of_num = nums[i] * nums[i]
        #     nums[i] = square_of_num
        # nums.sort()
        # return nums
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        for pos in range(len(nums) - 1, -1, -1):
            l = nums[left]
            r = nums[right]
            if l ** 2 > r ** 2:
                res[pos] = l ** 2
                left += 1
            else:
                res[pos] = r ** 2
                right -= 1
        return res