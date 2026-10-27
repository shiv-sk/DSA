class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        num3_set = set(nums3)
        result = (num1_set & num2_set) | (num1_set & num3_set) | (num2_set & num3_set)
        return list(result)