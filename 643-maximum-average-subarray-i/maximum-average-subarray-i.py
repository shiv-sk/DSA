class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # max_avg = float("-inf")
        # for i in range(len(nums)):
        #     j = i
        #     sum = 0
        #     cntr = 0
        #     while j < len(nums) and cntr < k:
        #         sum += nums[j]
        #         cntr += 1
        #         j += 1
        #     if cntr == k:
        #         current_avg = sum / k
        #         max_avg = max(max_avg, current_avg)
        # return max_avg
        left = 0
        window_sum = 0
        max_avg = float("-inf")
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == k:
                avg_sum = window_sum / k
                max_avg = max(avg_sum, max_avg)
                window_sum -= nums[left]
                left += 1
            
        return max_avg