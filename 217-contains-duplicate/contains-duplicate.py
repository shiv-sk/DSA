class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return True
        #     nums_set.add(num)
        # return False
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                return True
            i += 1
        return False