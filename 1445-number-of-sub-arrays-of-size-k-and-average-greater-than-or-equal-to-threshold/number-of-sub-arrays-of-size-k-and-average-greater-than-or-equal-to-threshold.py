class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left = 0
        count = 0
        window_sum = 0
        for right in range(len(arr)):
            window_sum += arr[right]
            if right - left + 1 == k:
                avg_sum = window_sum // k
                if avg_sum >= threshold:
                    count += 1
                window_sum -= arr[left]
                left += 1
        return count