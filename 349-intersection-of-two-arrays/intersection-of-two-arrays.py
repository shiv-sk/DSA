class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_list = set(nums2)
        res = []
        for num in nums1:
            if num in set_list:
                res.append(num)
                set_list.remove(num)
        return res