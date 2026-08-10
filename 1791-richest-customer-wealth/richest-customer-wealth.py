class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            current_wealth = sum(accounts[i])
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth