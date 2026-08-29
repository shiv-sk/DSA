class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set_list = set(nums2)
        # res = []
        # for num in nums1:
        #     if num in set_list:
        #         res.append(num)
        #         set_list.remove(num)
        # return res
        nums1.sort()
        nums2.sort()
        i = 0 
        j = 0
        res = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j]:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res