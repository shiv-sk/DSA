class Solution:
    def countFreq(self, arr, target):
        # code here
        def find_first(arr, target):
            low, high = 0, len(arr) - 1
            first_idx = -1
            while (low <= high):
                mid = (low + high) // 2
                if arr[mid] == target:
                    first_idx = mid
                    high = mid - 1
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return first_idx
        def find_last(arr, target):
            low, high = 0, len(arr) - 1
            last_idx = -1
            while (low <= high):
                mid = (low + high) // 2
                if arr[mid] == target:
                    last_idx = mid
                    low = mid + 1
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return last_idx
        first = find_first(arr, target)
        if first == -1:
            return 0
        last = find_last(arr, target)
        return (last - first) + 1
        
                    