class Solution:
    def firstRepeated(self,arr):
        # code here
        repeating_ele = {}
        for num in arr:
            repeating_ele[num] = repeating_ele.get(num, 0) + 1
        for i in range(len(arr)):
            num = arr[i]
            if num in repeating_ele and repeating_ele[num] > 1:
                return i+1
        return -1
        