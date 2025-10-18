class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        result = []
        for customer in accounts:
            total = sum(customer)
            result.append(total)
        return max(result)
        