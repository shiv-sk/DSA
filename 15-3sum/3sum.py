class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        st = set()
        i = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum == 0:
                    st.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1
        result = [ele for ele in st if ele]
        return result