class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list_map = {}
        ans = []
        least_sum = float('inf')
        for i in range(len(list1)):
            list_map[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in list_map:
                current_sum = j + list_map[list2[j]]
                if current_sum < least_sum:
                    least_sum = current_sum
                    ans = [list2[j]]
                elif current_sum == least_sum:
                    ans.append(list2[j])
        return ans