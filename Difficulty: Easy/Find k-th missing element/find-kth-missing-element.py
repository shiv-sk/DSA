class Solution:

    def findKthMissing(self, arr1, arr2, k):
        # code here
        missing_count = -1
        count = 0
        normal_set = set()
        for num in arr2:
            normal_set.add(num)
        for num in arr1:
            if num not in normal_set:
                count += 1
                if count == k:
                    return num
        return missing_count
