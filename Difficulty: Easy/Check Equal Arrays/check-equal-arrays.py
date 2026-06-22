class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        counter_map = {}
        for num in a:
            counter_map[num] = counter_map.get(num, 0) + 1
        for num in b:
            if num not in counter_map or counter_map[num] == 0:
                return False
            counter_map[num] = counter_map[num] - 1
        return True