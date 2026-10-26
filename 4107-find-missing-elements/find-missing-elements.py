class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        min_num = min(nums)
        max_num = max(nums)
        return [x for x in range(min_num + 1, max_num) if x not in nums_set]