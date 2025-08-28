class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acc = []
        
        for row in accounts:
            acc.append(sum(row))
        return max(acc)