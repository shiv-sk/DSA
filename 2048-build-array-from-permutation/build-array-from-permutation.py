class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            ans.append(nums[nums[i]])
            i += 1
        return ans       